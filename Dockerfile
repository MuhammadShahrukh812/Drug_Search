# Use an official Python image as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update 

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port that the app will run on
EXPOSE 5000
