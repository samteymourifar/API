# Use an official Python runtime (Alpine version) as a parent image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app


# Install Python dependencies
RUN pip install -r requirements.txt

COPY requirements.txt  /app

# Copy the current directory contents into the container at /app
COPY . /app


# Expose the port that the app runs on
EXPOSE 5000


# Run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
