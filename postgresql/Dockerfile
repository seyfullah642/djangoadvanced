FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /postgresql

#Install dependencies
RUN python3 -m pip install Django \
    && python3 -m pip install psycopg2-binary==2.8.4

# Copy project
COPY . /postgresql/