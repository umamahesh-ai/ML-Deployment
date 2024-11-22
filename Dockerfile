# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt first, so that we can install dependencies separately (this helps caching)
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]

