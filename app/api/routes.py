from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.models import Movie, IndexResponse
from app.services.elasticsearch_service import ElasticsearchService
from app.services.movie_service import fetch_movies

router = APIRouter(prefix="/api/movies", tags=["movies"])

@router.post("/index", response_model=IndexResponse)
async def index_movies(
    title: Optional[str] = Query(None, description="Title substring to filter movies")
):
    """
    Index movies from the external API into Elasticsearch.
    If no title is provided, it will fetch all movies.
    """
    try:
        # Initialize services
        es_service = ElasticsearchService()
        
        # Fetch and index movies
        movies = await fetch_movies(title or "")
        await es_service.index_movies(movies)
        
        # Cleanup
        await es_service.close()
        
        return IndexResponse(
            message="Successfully indexed movies",
            count=len(movies)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search", response_model=List[Movie])
async def search_movies(
    title: Optional[str] = Query(None, description="Title substring to search for"),
    year: Optional[int] = Query(None, description="Exact year to match")
):
    """
    Search for movies in the index by title and/or year.
    At least one parameter must be provided.
    """
    if not title and year is None:
        raise HTTPException(
            status_code=400,
            detail="At least one search parameter (title or year) is required"
        )
    
    try:
        # Initialize services
        es_service = ElasticsearchService()
        
        # Search movies
        movies = await es_service.search_movies(title, year)
        
        # Cleanup
        await es_service.close()
        
        return movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))