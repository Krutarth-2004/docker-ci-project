from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello CI!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#Dockerfile
# # 1. Use a specific, slim base image
# FROM python:3.9-slim

# # 2. Set working directory
# WORKDIR /app 

# # 3. Copy dependency file first (for caching)
# COPY requirements.txt .

# # 4. Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # 5. Copy application code
# COPY . .

# # 6. Create non-root user for security
# RUN useradd -r appuser
# USER appuser

# # 7. Expose application port
# EXPOSE 5000

# # 8. Run the application
# CMD ["python", "app.py"]

#requirements.txt
#flask
#pytest

#tests/test_app.py
# def test_sample():
#     assert 1 == 1

#.github/workflows/ci.yml
# name: Docker CI Pipeline

# on:
#   push:
#     branches: [ main ]
#   pull_request:
#     branches: [ main ]

# jobs:
#   lint:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v4
#       - name: Lint Dockerfile
#         run: echo "Lint step (placeholder)"

#   test:
#     needs: lint
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v4
#       - uses: actions/setup-python@v5
#         with:
#           python-version: "3.11"
#       - run: pip install -r requirements.txt
#       - run: pytest

#   build:
#     needs: test
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v4
#       - run: docker build -t myapp .

