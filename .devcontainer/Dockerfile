FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python tools
RUN pip install --upgrade pip \
    && pip install pre-commit pytest black flake8 mypy

# Install project dependencies
COPY ../requirements.txt /workspace/requirements.txt
RUN pip install -r /workspace/requirements.txt || true

# Set up pre-commit hooks
RUN pre-commit install --install-hooks || true

WORKDIR /workspace
