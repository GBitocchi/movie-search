import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
from app.main import app
from app.services.elasticsearch_service import ElasticsearchService

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_movies_response():
    return {
        "page": 1,
        "per_page": 10,
        "total": 2,
        "total_pages": 1,
        "data": [
            {
                "Title": "The Difficult Test Movie",
                "Year": 2023,
                "imdbID": "tt2175527"
            },
            {
                "Title": "Another Difficult Test Movie",
                "Year": 2023,
                "imdbID": "tt6614221"
            }
        ]
    }

@pytest.fixture
def mock_es_service():
    class MockElasticsearchService:
        async def create_index(self):
            return None

        async def index_movies(self, movies):
            return True

        async def search_movies(self, title=None, year=None):
            return [
                {
                    "Title": "Difficult Test Movie",
                    "Year": 2023,
                    "imdbID": "tt2175527"
                }
            ]

        async def close(self):
            return None

    return MockElasticsearchService()