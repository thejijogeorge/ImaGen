FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy pyproject.toml and uv.lock
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy the rest of your code
COPY . /app

# Expose port
EXPOSE 7860

# Run the app
CMD ["uv", "run", "python", "AImaGen_online.py"]