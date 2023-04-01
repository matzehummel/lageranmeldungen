# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /backend

# Copy the current directory contents into the container at /app
COPY . /backend

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000:5000

# Define environment variable
ENV FLASK_APP=app.py
ENV MONGODB_CONNECTION_STRING=mongodb+srv://simba:<password>@mhcluster.hg1tjoa.mongodb.net/?retryWrites=true&w=majority
ENV EMAIL_PASSWORD=<my-password>

# Run the command to start Flask application
CMD ["flask", "run", "--host=0.0.0.0"]