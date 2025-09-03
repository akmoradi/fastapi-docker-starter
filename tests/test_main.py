# Import testing tools
from fastapi.testclient import TestClient   # Simulates HTTP requests
from app.main import app    # Our application

# Create a test client - like a fake browser
client = TestClient(app)

def test_health():
    """Test our health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200     # Should return "OK"
    assert response.json() == {"status": "OK"}

def test_root():
    """Test our root endpoint"""
    response = client.get("/")
    assert response.status_code == 200     # Should return "OK"
    assert "Hello, FastAPI" in response.json()["message"]

def test_create_item():
    """Test creating a new item"""
    # Prepare test data
    test_item = {
        "name": "Test Book",
        "price": 19.99,
        "is_offer": True
    }

    # Send POST request
    response = client.post("/items", json=test_item)

    # Check the response
    assert response.status_code == 200
    data = response.json()
    assert data["created"] ["name"] == "Test Book"
    assert data["message"] == "Item created successfully!"


