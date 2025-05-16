# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local files into the container
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Tkinter
RUN apt-get update && apt-get install -y python3-tk

# Command to run the application
CMD ["python", "weather_app.py"]