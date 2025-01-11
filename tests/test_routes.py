import pytest
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_index_movies_success(client, mock_movies_response, mock_es_service):
    with patch('app.api.routes.ElasticsearchService', return_value=mock_es_service), \
         patch('app.api.routes.fetch_movies', return_value=[{
             "Title": "Difficult Test Movie",
             "Year": 2023,
             "imdbID": "tt2175527"
         }]):
        
        response = client.post("/api/movies/index")
        assert response.status_code == 200
        assert "Successfully indexed" in response.json()["message"]

@pytest.mark.asyncio
async def test_search_movies_success(client, mock_es_service):
    with patch('app.api.routes.ElasticsearchService', return_value=mock_es_service):
        response = client.get("/api/movies/search", params={"title": "test"})
        assert response.status_code == 200
        assert isinstance(response.json(), list)

def test_search_movies_no_params(client):
    response = client.get("/api/movies/search")
    assert response.status_code == 400