# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install requests

# Set the default command to execute when the container starts
CMD ["python", "movie_assets_downloader.py"]
