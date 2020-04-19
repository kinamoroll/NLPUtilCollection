
FROM python:3.11-slim

# lint it:
# $ docker run --rm -i hadolint/hadolint < Dockerfile

# hadolint ignore=DL3008
RUN apt-get update -y && apt-get install -y --no-install-recommends git gcc g++ curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
