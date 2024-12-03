from pydantic import BaseModel


class CorsConfig(BaseModel):
    allow_origins: list[str] = ['*']
    allow_credentials: bool = True
    allow_methods: list[str] = ['*']
    allow_headers: list[str] = ['*']


class APIConfig(BaseModel):
    title: str = 'YOUR API TITLE'
    root_path: str = '/api'
    docs_url: str = '/docs'
    description: str = 'YOUR API DESCRIPTION'
    cors: CorsConfig = CorsConfig()
