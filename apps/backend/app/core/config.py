"""
Application Configuration
Learning Focus: Environment variables, settings management, security

This module handles all application configuration using Pydantic Settings.
You'll learn:
- Environment variable management
- Configuration validation
- Security best practices
- Different environment setups (dev, staging, prod)

Date: July 2025
"""

from pydantic_settings import BaseSettings
from pydantic import Field, validator
from typing import List, Optional
import secrets
from functools import lru_cache

class Settings(BaseSettings):
    """
    Application settings with validation
    Learning: Pydantic BaseSettings automatically loads from environment variables
    """
    
    # Project Information
    PROJECT_NAME: str = "Commute Tracker Learning Project"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Learning FastAPI through building a commute tracker"
    
    # Environment
    ENVIRONMENT: str = Field(default="development", description="Environment: development, staging, production")
    DEBUG: bool = Field(default=True, description="Debug mode for development")
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = Field(
        default_factory=lambda: secrets.token_urlsafe(32),
        description="Secret key for JWT token signing"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = Field(
        default="postgresql://user:password@localhost:5432/commute_tracker",
        description="Database connection URL"
    )
    
    # Redis
    REDIS_URL: str = Field(
        default="redis://localhost:6379",
        description="Redis connection URL for caching"
    )
    
    # External APIs
    GOOGLE_MAPS_API_KEY: Optional[str] = Field(
        default=None,
        description="Google Maps API key for route calculations"
    )
    
    # CORS Settings
    BACKEND_CORS_ORIGINS: List[str] = Field(
        default=[
            "http://localhost:3000",
            "http://localhost:8080", 
            "http://127.0.0.1:3000",
            "http://127.0.0.1:8080"
        ],
        description="List of allowed CORS origins"
    )
    
    # Security Headers
    ALLOWED_HOSTS: List[str] = Field(
        default=["localhost", "127.0.0.1", "0.0.0.0"],
        description="Allowed hosts for security"
    )
    
    # Logging
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = Field(default=20, ge=1, le=100)
    MAX_PAGE_SIZE: int = Field(default=100, ge=1, le=1000)
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = Field(default=60, description="API calls per minute per IP")
    
    # Learning: Validators for configuration validation
    @validator("ENVIRONMENT")
    def validate_environment(cls, v):
        """Learning: Custom validator to ensure valid environment values"""
        allowed = ["development", "staging", "production"]
        if v not in allowed:
            raise ValueError(f"Environment must be one of: {allowed}")
        return v
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v):
        """Learning: Validator to handle CORS origins from environment variable"""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    @validator("SECRET_KEY")
    def validate_secret_key(cls, v):
        """Learning: Ensure secret key is secure enough"""
        if len(v) < 32:
            raise ValueError("Secret key must be at least 32 characters long")
        return v
    
    @validator("GOOGLE_MAPS_API_KEY")
    def validate_google_maps_key(cls, v):
        """Learning: Basic validation for Google Maps API key format"""
        if v and (len(v) < 20 or not v.startswith("AIza")):
            raise ValueError("Invalid Google Maps API key format")
        return v
    
    # Learning: Property methods for computed values
    @property
    def is_development(self) -> bool:
        """Check if running in development mode"""
        return self.ENVIRONMENT == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode"""
        return self.ENVIRONMENT == "production"
    
    @property
    def database_config(self) -> dict:
        """Get database configuration dictionary"""
        return {
            "url": self.DATABASE_URL,
            "echo": self.DEBUG,  # Log SQL queries in debug mode
            "future": True,      # Use SQLAlchemy 2.0 style
        }
    
    # Learning: Configuration for different environments
    class Config:
        # Learning: This tells Pydantic to read from .env file
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        
        # Learning: Field aliases for different naming conventions
        fields = {
            "DATABASE_URL": {"env": ["DATABASE_URL", "DB_URL"]},
            "REDIS_URL": {"env": ["REDIS_URL", "CACHE_URL"]},
        }


# Learning: Cached settings instance (singleton pattern)
@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance
    Learning: lru_cache ensures we only create one Settings instance
    This is important for performance and consistency
    """
    return Settings()


# Learning: Environment-specific configurations
class DevelopmentSettings(Settings):
    """Development-specific settings"""
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"
    
    class Config(Settings.Config):
        env_file = ".env.development"


class ProductionSettings(Settings):
    """Production-specific settings"""
    DEBUG: bool = False
    LOG_LEVEL: str = "WARNING"
    
    class Config(Settings.Config):
        env_file = ".env.production"


def get_settings_for_environment(env: str) -> Settings:
    """
    Get settings for specific environment
    Learning: Factory pattern for different configurations
    """
    settings_map = {
        "development": DevelopmentSettings,
        "production": ProductionSettings,
    }
    
    settings_class = settings_map.get(env, Settings)
    return settings_class()


# Learning: Export commonly used settings
settings = get_settings()

# Learning: Configuration validation on import
if __name__ == "__main__":
    """
    Learning: This allows testing configuration by running: python -m app.core.config
    """
    print("🔧 Configuration Validation")
    print(f"Project: {settings.PROJECT_NAME}")
    print(f"Environment: {settings.ENVIRONMENT}")
    print(f"Debug: {settings.DEBUG}")
    print(f"Database URL: {settings.DATABASE_URL}")
    print(f"API Version: {settings.API_V1_STR}")
    print(f"CORS Origins: {settings.BACKEND_CORS_ORIGINS}")
    print("✅ Configuration valid!")