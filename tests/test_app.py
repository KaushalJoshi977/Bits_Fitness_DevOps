
import pytest
from app import app, PROGRAMS


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


# Test 1: Homepage
def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"ACEest Fitness" in response.data


# Test 2: Health check
def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


# Test 3: Get all programs
def test_get_all_programs(client):
    response = client.get("/api/programs")

    assert response.status_code == 200
    assert len(response.json) == 3


# Test 4-6: Individual fitness programs
@pytest.mark.parametrize("slug", [
    "fat-loss",
    "muscle-gain",
    "beginner"
])
def test_valid_program(client, slug):
    response = client.get(f"/api/programs/{slug}")

    assert response.status_code == 200
    assert response.json["name"] == PROGRAMS[slug]["name"]


# Test 7: Invalid fitness program
def test_invalid_program(client):
    response = client.get("/api/programs/invalid")

    assert response.status_code == 404
    assert response.json["error"] == "Program not found"


# Test 8: Validate program data structure
def test_program_structure():
    for program in PROGRAMS.values():
        assert "name" in program
        assert "workout" in program
        assert "diet" in program

        assert program["name"]
        assert program["workout"]
        assert program["diet"]
