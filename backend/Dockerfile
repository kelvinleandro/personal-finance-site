FROM python:3.12.10-alpine3.21

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache \
  postgresql-dev \
  gcc \
  musl-dev

COPY requirements.txt .
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]