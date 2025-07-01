"""
Logging configuration for the Commute Tracker API
Learning: Structured logging setup with different levels and formats
"""

import logging
import sys
from typing import Any, Dict

import structlog
from structlog.stdlib import LoggerFactory


def setup_logging() -> None:
    """
    Configure structured logging for the application
    
    Learning:
    - Structured logging with structlog
    - Different log levels for different environments
    - Console and file logging
    - JSON formatting for production
    """
    
    # Learning: Configure structlog
    structlog.configure(
        processors=[
            # Learning: Add timestamp and log level
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            # Learning: JSON formatting for structured logging
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    # Learning: Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )
    
    # Learning: Set specific logger levels
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    
    # Learning: Create a logger instance
    logger = structlog.get_logger()
    logger.info("📝 Logging configured successfully")


def get_logger(name: str = None) -> Any:
    """
    Get a structured logger instance
    
    Args:
        name: Logger name (optional)
        
    Returns:
        Structured logger instance
    """
    return structlog.get_logger(name)


# Learning: Example usage of structured logging
if __name__ == "__main__":
    setup_logging()
    logger = get_logger(__name__)
    
    # Learning: Different log levels
    logger.debug("Debug message", extra_field="debug_value")
    logger.info("Info message", user_id=123, action="login")
    logger.warning("Warning message", issue="deprecated_feature")
    logger.error("Error message", error_code=500, user_id=456)
    
    # Learning: Exception logging
    try:
        1 / 0
    except Exception as e:
        logger.exception("Division by zero error", dividend=1, divisor=0) 