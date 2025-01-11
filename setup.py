from setuptools import setup, find_packages

setup(
    name="movie-search",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "elasticsearch>=7.0.0",
        "httpx>=0.24.0",
        "pydantic>=2.0.0",
        "pydantic-settings>=2.0.0",
    ],
)