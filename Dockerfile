# Use an official Python runtime as a parent image
FROM python:3

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /usr/src/vendo

RUN pip install --upgrade pip

# Copy the project-level requirements.txt to install project dependencies
COPY ./requirements.txt /usr/src/vendo/requirements.txt

# Install project-level dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /usr/src/vendo/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=core.settings

# Run Django migrations and start the development server
#CMD ["python", "manage.py", "makemigrations"]
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
