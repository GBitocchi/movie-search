from elasticsearch import AsyncElasticsearch
from typing import List, Optional
from app.models import Movie
from app.config import settings

class ElasticsearchService:
    def __init__(self):
        self.es = AsyncElasticsearch([
            f'http://{settings.ELASTICSEARCH_HOST}:{settings.ELASTICSEARCH_PORT}'
        ])
        self.index_name = "movies"

    async def create_index(self) -> None:
        """Create the movies index if it doesn't exist"""
        if not await self.es.indices.exists(index=self.index_name):
            await self.es.indices.create(
                index=self.index_name,
                body={
                    "mappings": {
                        "properties": {
                            "Title": {"type": "text"},
                            "Year": {"type": "integer"},
                            "imdbID": {"type": "keyword"}
                        }
                    }
                }
            )

    async def index_movies(self, movies: List[Movie]) -> bool:
        """Index a list of movies"""
        try:
            # Delete existing index
            await self.es.indices.delete(index=self.index_name, ignore=[404])
            await self.create_index()
            
            # Index movies
            for movie in movies:
                await self.es.index(
                    index=self.index_name,
                    document=movie.dict(),
                    id=movie.imdbID
                )
            await self.es.indices.refresh(index=self.index_name)
            return True
        except Exception as e:
            print(f"Error indexing movies: {str(e)}")
            raise

    async def search_movies(self, title: Optional[str] = None, year: Optional[int] = None) -> List[Movie]:
        """Search for movies by title and/or year"""
        try:
            query = {"bool": {"must": []}}
            
            if title:
                query["bool"]["must"].append({"match": {"Title": title}})
            if year:
                query["bool"]["must"].append({"term": {"Year": year}})
                
            result = await self.es.search(
                index=self.index_name,
                body={"query": query}
            )
            
            return [Movie(**hit["_source"]) for hit in result["hits"]["hits"]]
        except Exception as e:
            print(f"Error searching movies: {str(e)}")
            raise

    async def close(self) -> None:
        """Close the Elasticsearch connection"""
        await self.es.close()