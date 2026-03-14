# 🐳 Docker Lab 1 - Dockerized Flask Application

A simple Flask web application containerized using Docker. This lab demonstrates how to build and run a Python web application inside a Docker container.

## 📁 Project Structure

```
docker-lab1/
├── app.py           # Flask application
├── Dockerfile       # Docker image instructions
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Python 3.9+

### Build the Docker Image
```bash
docker build -t docker-lab1 .
```

### Run the Container
```bash
docker run -p 8080:5000 docker-lab1
```

## 🌐 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Homepage with navigation links |
| `/health` | Health check - returns app status |
| `/info` | System info - Python version, platform, architecture |
| `/time` | Returns the current server time |

## 📸 Screenshots

### Home Page
Visit `http://localhost:8080` to see the homepage.

### Health Check
Visit `http://localhost:8080/health` for a JSON health status response.

### System Info
Visit `http://localhost:8080/info` for system information.

### Current Time
Visit `http://localhost:8080/time` for the current server time.

## 🛠️ Modifications from Original Lab
- Added `/health` endpoint returning JSON status
- Added `/info` endpoint displaying system/environment details
- Added `/time` endpoint returning the current datetime
- Added a styled HTML homepage with navigation links

## 📚 What I Learned
- How to write a `Dockerfile` to containerize a Python application
- How to build and run Docker images
- How to expose and map container ports
- How Flask routes work inside a container