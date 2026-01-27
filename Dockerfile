# 1. Use a specific, slim base image
FROM python:3.9-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy dependency file first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY . .

# 6. Create non-root user for security
RUN useradd -r appuser
USER appuser

# 7. Expose application port
EXPOSE 5000

# 8. Run the application
CMD ["python", "app.py"]