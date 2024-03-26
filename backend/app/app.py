import uvicorn
import os

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, HTTPException
from config import config

from fastapi.middleware.cors import CORSMiddleware

from util.response import wrap_respponse, status

from repository import SessionLocal, engine
from repository.schemas import Base

app = FastAPI(docs_url='/api/docs' if not config['PROD'] else None,
              redoc_url='/api/redoc' if not config['PROD'] else None,
              openapi_url='/api/openapi.json' if not config['PROD'] else None)


app.add_middleware(
    CORSMiddleware,
    allow_origins=config['ALLOWED_HOSTS'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = wrap_respponse(
        status.HTTP_500_INTERNAL_SERVER_ERROR, "internal server error", {})
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


for route in os.listdir('./routes'):
    if route.startswith('_') or not route.endswith('.py'):
        continue
    module_name = route.removesuffix('.py')
    module = __import__(f"routes.{module_name}", fromlist=[module_name])
    app.include_router(module.router, prefix=f"/api/{module_name}", tags=[module_name])

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return wrap_respponse(exc.status_code, exc.detail, exc.headers)

@app.exception_handler(RequestValidationError)
async def http_exception_handler(request, exc):
    return wrap_respponse(status.HTTP_422_UNPROCESSABLE_ENTITY, "invalid request" ,exc.errors())

if __name__ == "__main__":
    configs = {
        'host': config['HOST'],
        'port': config['PORT'],
        'reload': not config['PROD'],
        'workers': config['workers'] if config['PROD'] else 1
    }
    uvicorn.run("app:app", **configs)