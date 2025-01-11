from fastapi import FastAPI
from app.api.routes import router
from app.services.elasticsearch_service import ElasticsearchService
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create Elasticsearch index
    es_service = ElasticsearchService()
    await es_service.create_index()
    yield
    # Shutdown: Close Elasticsearch connection
    await es_service.close()

app = FastAPI(
    title="Movie Search API",
    description="API for indexing and searching movies",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}