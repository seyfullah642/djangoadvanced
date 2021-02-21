FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /books

# Copy project
COPY . /books/

#Install dependencies
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt