# Setup environment
FROM alpine:latest
RUN apk update

# Setup workspace
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .

# Install all dependencies
RUN \
 apk add --no-cache python3 py3-pip postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 pip3 install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# Start app
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]