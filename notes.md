Dockerfile

# Dockerfile
FROM python:3.11-slim

# Prevents python from writing .pyc files and buffers logs nicely
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps:
# - build-essential: gcc, g++, make (to compile C)
# - (optional) git, curl for debugging
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    make \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy and install python dependencies first (better caching)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the repository
COPY . /app

# Build the C aggregator
# Assumes: c_aggregator/Makefile builds bin/aggregator
RUN make -C c_aggregator

# Streamlit default port
EXPOSE 8501

# Streamlit needs these for container environments
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app/app.py"]
