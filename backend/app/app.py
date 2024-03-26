import uvicorn
import os

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, HTTPException
from config import config

from fastapi.middleware.cors import CORSMiddleware

from util.response import wrap_response, status

from repository import SessionLocal

app = FastAPI(docs_url='/api/docs', redoc_url='/api/redoc',
              openapi_url='/api/openapi.json')


app.add_middleware(
    CORSMiddleware,
    allow_origins=config['ALLOWED_HOSTS'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = wrap_response(
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
    return wrap_response(exc.status_code, exc.detail, {})

@app.exception_handler(RequestValidationError)
async def http_exception_handler(request, exc):
<<<<<<< HEAD
    return wrap_response(status.HTTP_422_UNPROCESSABLE_ENTITY, "invalid request" ,exc.errors())
=======
    return wrap_respponse(status.HTTP_422_UNPROCESSABLE_ENTITY, "invalid request" ,exc.errors())
>>>>>>> 94d563b (remove Base.metadata.create_all(bind=engine))

if __name__ == "__main__":
    configs = {
        'host': config['HOST'],
        'port': config['PORT'],
        'reload': not config['PROD'],
        'workers': config['workers'] if config['PROD'] else 1
    }
    uvicorn.run("app:app", **configs)