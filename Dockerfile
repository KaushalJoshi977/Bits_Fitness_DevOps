
# Use a lightweight Python image
FROM python:3.12-slim

# Python environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set application working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user
RUN useradd --uid 10001 --create-home appuser

# Copy application and tests
COPY --chown=appuser:appuser app.py .
COPY --chown=appuser:appuser tests/ ./tests/

# Run the application as non-root
USER appuser

# Application port
EXPOSE 5000

# Start Flask through Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
