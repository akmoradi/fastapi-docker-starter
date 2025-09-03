# FastAPI Docker Starter

My first web API build with FastAPI, Docker, and modern Python practices.

## What This Project Does

This is a simple REST API that can:
- Return a welcome message
- Check if the service is healthy
- Create and retrieve items with name, price, and offer status
- Automatically generate interactive documentation

## Technologies Used

- **FastAPI**: Modern Python web framework
- **Uvicorn**: ASGI web server
- **Docker**: Containerization
- **Pytest**: Testing framework
- **Git/GitHub**: Version control

## How to Run Locally

### Prerequisites
- Python 3.11+ or 3.12
- Git
- Docker Desktop

### Setup

1. Clone this repository:
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\Acticate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

5. Open your browser:
- Main app: http://127.0.0.1:8000
- Interactive docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Testing

Run tests with:
```bash
pytest -v
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /items/{item_id}` - Get item by ID
- `POST /items` - Create new item

## Project Structure

```
fastapi-docker-starter/
├── app/
│   └── main.py          # Main application code
├── tests/
│   └── test_main.py     # Test cases
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
└── README.md            # This file
```

## Learning Journey

This project was created as part of learning:
- Web API development with FastAPI
- containerization with Docker
- Version control with Git/GitHub
- Test-driven development with Pytest

## Next Steps

- [ ] Add database integration
- [ ] Add authentication
- [ ] Add more comprehensive error handling
- [ ] Deploy to cloud platform

---

Built with ❤ by akmoradi as a learning project 