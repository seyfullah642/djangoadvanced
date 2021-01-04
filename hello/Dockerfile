FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /hello

#Install dependencies
RUN python3 -m pip install Django

# Copy project
COPY . /hello/