"""
Database Configuration and Connection Management
Learning Focus: SQLAlchemy, async database operations, connection pooling

This module sets up database connections and sessions.
You'll learn:
- SQLAlchemy engine configuration
- Database session management
- Connection pooling
- Async database operations
- Dependency injection for database sessions

Date: July 2025
"""

from sqlalchemy import create_engine, event
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from .config import get_settings

# Learning: Get application settings
settings = get_settings()
logger = logging.getLogger(__name__)

# Learning: Create SQLAlchemy declarative base
# All your models will inherit from this
Base = declarative_base()

# Learning: Synchronous database engine (for migrations, admin tasks)
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Log SQL queries in debug mode
    future=True,          # Use SQLAlchemy 2.0 style
    pool_pre_ping=True,   # Validate connections before use
    pool_recycle=3600,    # Recycle connections every hour
    max_overflow=20,      # Allow up to 20 overflow connections
    pool_timeout=30,      # Timeout after 30 seconds
)

# Learning: Session factory for synchronous operations
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    future=True
)

# Learning: Async database engine (for FastAPI endpoints)
# Note: Replace 'postgresql://' with 'postgresql+asyncpg://' for async
async_database_url = settings.DATABASE_URL.replace(
    "postgresql://", 
    "postgresql+asyncpg://"
)

async_engine = create_async_engine(
    async_database_url,
    echo=settings.DEBUG,
    future=True,
    pool_pre_ping=True,
    pool_recycle=3600,
)

# Learning: Async session factory
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False  # Important for async operations
)

# Learning: Database event listeners for monitoring
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Learning: Event listener for database connections
    This is useful for setting database-specific configurations
    """
    if "sqlite" in settings.DATABASE_URL:
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
    
    logger.debug(f"📊 Database connection established: {connection_record}")

@event.listens_for(engine, "checkout")
def receive_checkout(dbapi_connection, connection_record, connection_proxy):
    """Learning: Monitor connection checkout from pool"""
    logger.debug("📤 Database connection checked out from pool")

@event.listens_for(engine, "checkin")
def receive_checkin(dbapi_connection, connection_record):
    """Learning: Monitor connection checkin to pool"""
    logger.debug("📥 Database connection returned to pool")

# Learning: Dependency for getting database sessions in endpoints
def get_db() -> Session:
    """
    Synchronous database session dependency
    Learning: This is used with FastAPI's Depends() for dependency injection
    
    Usage in endpoints:
    @app.get("/items/")
    def read_items(db: Session = Depends(get_db)):
        return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"❌ Database session error: {e}")
        db.rollback()
        raise
    finally:
        db.close()

async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Async database session dependency
    Learning: For async endpoints (recommended for FastAPI)
    
    Usage in endpoints:
    @app.get("/items/")
    async def read_items(db: AsyncSession = Depends(get_async_db)):
        result = await db.execute(select(Item))
        return result.scalars().all()
    """
    async with AsyncSessionLocal() as db:
        try:
            yield db
        except Exception as e:
            logger.error(f"❌ Async database session error: {e}")
            await db.rollback()
            raise
        finally:
            await db.close()

# Learning: Context manager for manual session management
@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Context manager for manual database session management
    Learning: Use this when you need a database session outside of endpoints
    
    Usage:
    async with get_db_session() as db:
        result = await db.execute(select(User))
        users = result.scalars().all()
    """
    async with AsyncSessionLocal() as db:
        try:
            yield db
        except Exception as e:
            logger.error(f"❌ Manual database session error: {e}")
            await db.rollback()
            raise

# Learning: Database utilities
class DatabaseManager:
    """
    Database management utilities
    Learning: Centralized database operations for admin tasks
    """
    
    @staticmethod
    def create_tables():
        """Create all database tables"""
        try:
            Base.metadata.create_all(bind=engine)
            logger.info("✅ Database tables created successfully")
        except Exception as e:
            logger.error(f"❌ Failed to create tables: {e}")
            raise
    
    @staticmethod
    def drop_tables():
        """Drop all database tables (use with caution!)"""
        try:
            Base.metadata.drop_all(bind=engine)
            logger.warning("⚠️ All database tables dropped")
        except Exception as e:
            logger.error(f"❌ Failed to drop tables: {e}")
            raise
    
    @staticmethod
    async def check_connection():
        """Check database connection health"""
        try:
            async with AsyncSessionLocal() as db:
                await db.execute("SELECT 1")
                logger.info("✅ Database connection healthy")
                return True
        except Exception as e:
            logger.error(f"❌ Database connection failed: {e}")
            return False
    
    @staticmethod
    def get_connection_info():
        """Get database connection information"""
        pool = engine.pool
        return {
            "url": str(engine.url).replace(engine.url.password or "", "***"),
            "pool_size": pool.size(),
            "checked_in": pool.checkedin(),
            "checked_out": pool.checkedout(),
            "overflow": pool.overflow(),
            "total_connections": pool.size() + pool.overflow()
        }

# Learning: Database health check function
async def check_database_health() -> dict:
    """
    Check database health for monitoring
    Learning: Health checks are important for production monitoring
    """
    try:
        start_time = time.time()
        
        # Test connection
        async with AsyncSessionLocal() as db:
            await db.execute("SELECT 1 as health_check")
        
        response_time = time.time() - start_time
        
        return {
            "status": "healthy",
            "response_time": round(response_time * 1000, 2),  # milliseconds
            "connection_info": DatabaseManager.get_connection_info()
        }
    except Exception as e:
        logger.error(f"❌ Database health check failed: {e}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "connection_info": None
        }

# Learning: Initialize database (called from main.py)
async def init_database():
    """
    Initialize database on startup
    Learning: This is called during application startup
    """
    try:
        # Check connection
        await DatabaseManager.check_connection()
        
        # Create tables (in production, use Alembic migrations instead)
        if settings.DEBUG:
            DatabaseManager.create_tables()
        
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        raise

# Learning: Cleanup function (called on shutdown)
async def close_database():
    """
    Close database connections on shutdown
    Learning: Proper cleanup prevents connection leaks
    """
    try:
        await async_engine.dispose()
        engine.dispose()
        logger.info("✅ Database connections closed")
    except Exception as e:
        logger.error(f"❌ Error closing database connections: {e}")

if __name__ == "__main__":
    """
    Learning: Test database configuration
    Run with: python -m app.core.database
    """
    import asyncio
    import time
    
    async def test_database():
        print("🔧 Testing Database Configuration")
        
        # Test connection
        health = await check_database_health()
        print(f"Health: {health}")
        
        # Test session creation
        async with get_db_session() as db:
            result = await db.execute("SELECT 1 as test")
            print(f"Query result: {result.scalar()}")
        
        print("✅ Database configuration test completed")
    
    asyncio.run(test_database())