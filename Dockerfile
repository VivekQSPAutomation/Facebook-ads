# Use the official Python image as a base image
FROM python:3.9.17-bookworm

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install additional dependencies, such as libpango and fonts-noto-color-emoji
RUN apt-get update && \
    apt-get install -y libpango1.0-0 fonts-noto-color-emoji && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Configure locale to use UTF-8
RUN apt-get update && \
    apt-get install -y locales && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8

# Set terminal environment
ENV TERM xterm-256color

# Command to run your application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 4 --timeout 0 app:app
