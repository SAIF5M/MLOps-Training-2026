# MLOps Task 3: From Notebooks to Production

This project transforms our Olist delivery prediction notebooks into a robust, containerized inference service using FastAPI, Docker, and structured Python modules[cite: 1].

## Project Structure
- `app/`: FastAPI application endpoints[cite: 1].
- `config/`: Centralized configuration files (`config.yaml`)[cite: 1].
- `src/`: Core Python modules for configuration loading, preprocessing, and inference[cite: 1].
- `tests/`: Unit and integration tests using Pytest[cite: 1].
- `Dockerfile` & `docker-compose.yml`: Containerization and service orchestration[cite: 1].

## How to Run from Zero

1. **Clone the repository and navigate to Task3.**
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt