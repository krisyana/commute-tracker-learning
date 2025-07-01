# Learning: Multi-stage Docker build for FastAPI application
# This Dockerfile shows best practices for Python containerization

# Stage 1: Build stage
FROM python:3.11-slim as builder

# Learning: Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Learning: Install system dependencies needed for Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Learning: Create virtual environment for isolation
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Learning: Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Learning: Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Stage 2: Production stage
FROM python:3.11-slim as production

# Learning: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PATH="/opt/venv/bin:$PATH"

# Learning: Install only runtime dependencies
RUN apt-get update && apt-get install -y \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Learning: Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Learning: Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Learning: Set working directory
WORKDIR /app

# Learning: Copy application code
COPY . .

# Learning: Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Learning: Switch to non-root user
USER appuser

# Learning: Expose port that the app runs on
EXPOSE 8000

# Learning: Health check for container monitoring
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Learning: Default command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

# Development stage (for development with hot reload)
FROM production as development

# Learning: Install development dependencies
USER root
RUN apt-get update && apt-get install -y \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

USER appuser

# Learning: Development command with hot reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]