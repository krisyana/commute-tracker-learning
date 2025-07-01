"""
FastAPI Main Application
Learning Focus: Application setup, middleware, routing, lifespan events

This is your FastAPI application entry point. Here you'll learn:
- How to create and configure a FastAPI app
- Middleware setup (CORS, security, logging)
- Router organization and API versioning
- Application lifecycle management
- Health checks and monitoring

Date: July 2025
Author: Learning Project
"""

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn
import time
import logging

# Import our application modules
from .core.config import get_settings
from .core.database import engine, SessionLocal
from .core.logging_config import setup_logging
from .models.database import Base
from .routes import commutes, analytics, auth, health

# Learning: Get application settings
settings = get_settings()

# Learning: Set up structured logging
setup_logging()
logger = logging.getLogger(__name__)

# Learning: Application lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan context manager
    Learning: Startup and shutdown events for initialization/cleanup
    """
    # Startup
    logger.info("🚀 Starting Commute Tracker API...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    
    try:
        # Learning: Create database tables
        # In production, you'd use Alembic migrations instead
        Base.metadata.create_all(bind=engine)
        logger.info("📊 Database tables created/verified")
        
        # Learning: You could add other startup tasks here:
        # - Cache warming
        # - External service health checks
        # - Background task initialization
        
    except Exception as e:
        logger.error(f"❌ Startup failed: {e}")
        raise
    
    # Application is ready
    logger.info("✅ Application startup complete")
    
    yield  # Application runs here
    
    # Shutdown
    logger.info("👋 Shutting down Commute Tracker API...")
    # Learning: Cleanup tasks would go here
    logger.info("✅ Shutdown complete")


def create_application() -> FastAPI:
    """
    Application factory pattern
    Learning: This pattern makes testing easier and allows multiple app configurations
    """
    
    # Learning: Create FastAPI instance with comprehensive configuration
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="""
        ## Commute Tracker Learning Project API
        
        A comprehensive FastAPI application for learning modern Python web development.
        
        ### What you'll learn:
        - RESTful API design patterns
        - Async programming with Python
        - Database operations with SQLAlchemy
        - External API integration (Google Maps)
        - Data analysis with Pandas
        - Authentication and security
        - Testing strategies
        
        ### Features:
        - 🚗 Commute tracking and analysis
        - 🗺️ Google Maps integration
        - 📊 Data insights and optimization
        - 🔐 User authentication
        - 📈 Performance analytics
        """,
        version="1.0.0",
        docs_url="/docs" if settings.DEBUG else None,  # Hide docs in production
        redoc_url="/redoc" if settings.DEBUG else None,
        openapi_url="/openapi.json" if settings.DEBUG else None,
        lifespan=lifespan
    )
    
    # Learning: Security middleware
    if not settings.DEBUG:
        app.add_middleware(
            TrustedHostMiddleware, 
            allowed_hosts=settings.ALLOWED_HOSTS
        )
    
    # Learning: CORS middleware for frontend communication
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    
    # Learning: Custom middleware for request logging and timing
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        """
        Learning: Custom middleware to log requests and measure response time
        """
        start_time = time.time()
        
        # Log incoming request
        logger.info(f"📥 {request.method} {request.url.path}")
        
        # Process request
        response = await call_next(request)
        
        # Calculate and log response time
        process_time = time.time() - start_time
        logger.info(f"📤 {request.method} {request.url.path} - {response.status_code} - {process_time:.3f}s")
        
        # Add timing header for debugging
        response.headers["X-Process-Time"] = str(process_time)
        
        return response
    
    # Learning: Include API routers with prefixes and tags
    # This organizes your API endpoints into logical groups
    
    # Health check routes (no prefix for simplicity)
    app.include_router(
        health.router,
        tags=["Health"]
    )
    
    # Authentication routes
    app.include_router(
        auth.router,
        prefix=settings.API_V1_STR + "/auth",
        tags=["Authentication"]
    )
    
    # Commute tracking routes
    app.include_router(
        commutes.router,
        prefix=settings.API_V1_STR + "/commutes",
        tags=["Commutes"]
    )
    
    # Analytics and insights routes
    app.include_router(
        analytics.router,
        prefix=settings.API_V1_STR + "/analytics",
        tags=["Analytics"]
    )
    
    # Learning: Global exception handler
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        """
        Learning: Global exception handling for better error responses
        """
        logger.error(f"❌ Unhandled exception: {exc}", exc_info=True)
        
        if settings.DEBUG:
            # In debug mode, return detailed error information
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal Server Error",
                    "detail": str(exc),
                    "type": type(exc).__name__,
                    "path": request.url.path
                }
            )
        else:
            # In production, return generic error message
            return JSONResponse(
                status_code=500,
                content={"error": "Internal Server Error"}
            )
    
    return app

# Learning: Create the application instance
app = create_application()

# Learning: Root endpoint with API information
@app.get("/", response_model=dict, summary="API Information")
async def root():
    """
    Root endpoint providing API information and learning objectives
    
    Learning objectives:
    - Basic endpoint structure
    - Response models and documentation
    - API versioning concepts
    """
    return {
        "message": "🚗 Welcome to Commute Tracker Learning Project API!",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT,
        "api_docs": "/docs" if settings.DEBUG else "Not available in production",
        "learning_objectives": [
            "Master FastAPI fundamentals and async patterns",
            "Learn database operations with SQLAlchemy",
            "Integrate external APIs (Google Maps)",
            "Implement authentication and security",
            "Practice data analysis with Pandas",
            "Build production-ready API endpoints"
        ],
        "next_steps": [
            "Check out /docs for interactive API documentation",
            "Start with /health endpoint to test connectivity",
            "Explore /api/v1/commutes for main features",
            "Review the learning log for daily progress tracking"
        ],
        "external_links": {
            "frontend": "http://localhost:3000",
            "api_docs": "http://localhost:8000/docs",
            "github_repo": "https://github.com/krisyana/commute-tracker-learning"
        }
    }

# Learning: Direct run configuration for development
if __name__ == "__main__":
    """
    Learning: This allows running the app directly with python main.py
    In production, you'd use a proper ASGI server like Gunicorn
    """
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level=settings.LOG_LEVEL.lower(),
        access_log=True
    )