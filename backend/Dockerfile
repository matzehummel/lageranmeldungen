# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Install wkhtmltopdf dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libxrender1 \
        libxext6 \
        libfontconfig1 \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libwebp-dev \
        zlib1g-dev \
        libfreetype6-dev \
        wget

# Download and install wkhtmltopdf
ENV WKHTMLTOPDF_VERSION=0.12.6
RUN wget -q https://github.com/wkhtmltopdf/packaging/releases/download/${WKHTMLTOPDF_VERSION}-1/wkhtmltox_${WKHTMLTOPDF_VERSION}-1.buster_amd64.deb && \
    apt-get install -y ./wkhtmltox_${WKHTMLTOPDF_VERSION}-1.buster_amd64.deb && \
    rm ./wkhtmltox_${WKHTMLTOPDF_VERSION}-1.buster_amd64.deb

# Set path to wkhtmltopdf executable as an environment variable
ENV WKHTMLTOPDF_PATH=/usr/local/bin/wkhtmltopdf

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
ENV EMAIL_PASSWORD=<password>

# Run the command to start Flask application
CMD ["flask", "run", "--host=0.0.0.0"]