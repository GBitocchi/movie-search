# Movie Search API - Marsie

For a technical interview at Marsie, we are creating a FastAPI application that provides REST endpoints for indexing and searching movies using Elasticsearch.

## Interviewee
- Name: Gustavo Ayrton Bitocchi
- Email: gustavoabitocchi@gmail.com

## Features
- Index movies from external API
- Search movies by title and year
- Elasticsearch integration
- Docker support
- Async operations

## Requirements
- Docker and Docker Compose
- Python 3.9+

## Quick Start

1. Clone the repository:
	git clone https://github.com/yourusername/movie-search.git
	cd movie-search

2. Modify environment file .env (if applicable):

3. Start the application:
	docker-compose up --build
The API will be available at http://localhost:8000

## API Endpoints
	### POST /api/movies/index
	Index movies from the external API into Elasticsearch.

	-Query Parameters:
	--title (optional): Filter movies by title
	--Response:
		{
  			"message": "Successfully indexed movies",
  			"count": 10
		}

        ### GET /api/movies/search
	Search for movies in the index.

	-Query Parameters:
	--title (optional): Search by title
	--year (optional): Search by exact year
	--Response:
		[
  			{
    				"Title": "Movie Title",
    				"Year": 2021,
    				"imdbID": "tt1234567"
  			}
		]

## API Documentation
Once the application is running, visit:

Swagger UI: http://localhost:8000/docs

<img width="1728" alt="Screenshot 2025-01-11 at 04 18 57" src="https://github.com/user-attachments/assets/ec588a3a-9f35-4edd-b8c9-66013660c71f" />

## Running Tests

	### Using Docker
		docker-compose run app pytest

	### Local Testing
		pip3 install -r requirements.txt
		pytest tests/
