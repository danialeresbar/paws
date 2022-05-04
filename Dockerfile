###############
# BUILD STAGE #
###############

FROM python:3.8.13-slim-buster AS builder

# Set some environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# System dependencies
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
COPY test-requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -r test-requirements.txt

###############
# FINAL STAGE #
###############

FROM python:3.8.13-slim-buster AS runner

# Application dependencies
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    gdal-bin \
    python3-gdal \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Copy pip install results from builder image
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/

# Setup workdir
RUN mkdir /src
WORKDIR /src

# Copy the project files
COPY .coveragerc .
COPY apps/ apps/
COPY paws/ paws/
COPY scripts/ scripts/
COPY manage.py .
COPY requirements.txt .
