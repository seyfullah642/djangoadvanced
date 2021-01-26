FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /books

#Install dependencies
RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install Django \
    && python3 -m pip install psycopg2-binary==2.8.4 \
    && python3 -m pip install django-crispy-forms==1.8.1 \
    && python3 -m pip install django-allauth==0.41.0

# Copy project
COPY . /books/