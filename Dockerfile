# Use the official Python image as the base image
FROM python:3.9-slim-buster

ARG CI=""
ARG MAILGUN_DOMAIN=""
ARG MAILGUN_API_KEY=""
ARG SENDER_EMAIL=""
ARG TO_EMAIL=""

# Set the working directory
WORKDIR /src

# Install Poetry
RUN pip install poetry

# Copy the poetry files
COPY pyproject.toml poetry.lock* /src/

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Set up environment variables
RUN echo "CI=${CI}" >> .env
RUN echo "MAILGUN_DOMAIN=${MAILGUN_DOMAIN}" >> .env
RUN echo "MAILGUN_API_KEY=${MAILGUN_API_KEY}" >> .env
RUN echo "SENDER_EMAIL=${SENDER_EMAIL}" >> .env
RUN echo "TO_EMAIL=${TO_EMAIL}" >> .env

# Copy the rest of the project
COPY . .

# Run the command to start the application
CMD ["poetry", "run", "python", "main.py", "-t", "api"]
