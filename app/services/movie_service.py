import httpx
from typing import List
from app.models import Movie
from app.config import settings

async def fetch_movies(title: str = "") -> List[Movie]:
    """Fetch movies from external API"""
    all_movies = []
    page = 1
    
    async with httpx.AsyncClient() as client:
        while True:
            # Make API request
            params = {"Title": title, "page": page}
            response = await client.get(settings.MOVIES_API_BASE_URL, params=params)
            data = response.json()
            
            # Process movies
            movies = data.get("data", [])
            if not movies:
                break
                
            all_movies.extend([Movie(**movie) for movie in movies])
            
            # Check if we need to fetch more pages
            total_pages = data.get("total_pages", 1)
            if page >= total_pages:
                break
                
            page += 1
            
    return all_movies