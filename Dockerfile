# Use an official lightweight Python image as the base image
FROM python:3.9-slim

# Specify your e-mail address as the maintainer of the container image
LABEL maintainer="petrovav971@gmail.com"

# Set the working directory in the container to /app
WORKDIR /app

# Copy the local directory contents to the container's working directory
COPY . /app

# Install the Python packages specified by requirements.txt into the container
RUN apt update -y && apt install -y python3-pip && pip3 install -r requirements.txt

# Make port available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PORT=8000

# Run gunicorn when the container launches
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
