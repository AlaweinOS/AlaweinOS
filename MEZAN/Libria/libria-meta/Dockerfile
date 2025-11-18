FROM python:3.11-slim

WORKDIR /app

# System deps (optional: add build tools if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Copy code
COPY . /app/

# Install Python deps
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir pytest

EXPOSE 8081

CMD ["python", "-m", "libria_meta.services.mezan_orchestrator"]

