# API Starter Kit

An example project to demonstrate the use of Flask in a development environment with CI/CD tools like docker and docker-compose

The project contains its own containerized database which can be used to run and test the application in a standalone environment

To run:

```
docker-compose up --build
```

The API is accessible on port 8080 (frontend coming soon)

Currently, testing is done manually using server/tests/manual_tests/run_tests.py

