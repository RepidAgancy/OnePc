# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Set environment variable for Django to use production settings
ENV PYTHONUNBUFFERED 1

# Expose the port that Django will run on
EXPOSE 8001

# Run Django development server (use gunicorn for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
