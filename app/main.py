from fastapi import FastAPI
import uvicorn

from app.api.routers import router

app = FastAPI(
    openapi_tags=[
        {"name": "Users", "description": "Users endpoints"},
        {'name' : 'Admin', 'description' : 'Admin endpoints'}
    ]
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'app.main:app', 
        reload=True, 
        host='0.0.0.0',
        port=8000
)
