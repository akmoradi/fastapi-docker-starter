# syntax=docker/dockerfile:1

# Start from a base Python image
# This is like choosing the foundation for our house
FROM python:3.12-slim

# Set environment variables
# These optimize Python for containers
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CASHE-DIR=1

# Set working directory inside container
# This is like choosing which room we work in
WORKDIR /app

# Install system dependencies (minimal for this project)
# Update package list and clean up to keep image small
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm /rf /var/lib/apt/lists/*

# Copy and install Python dependencies first
# We do this before copying code for better Docker layer cashing
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Copy our application code
COPY app ./app

# Expose the port our app runs on
# This tells Docker which port to make available
EXPOSE 8000

# Command to run our application
# This is what happens when the container starts
CMD ["uvicorn", "app.main.py:app", "--host", "0.0.0.0", "--port", "8000"]
