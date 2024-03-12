import os
import uvicorn
from fastapi import FastAPI
from config import config

from fastapi_sqlalchemy import DBSessionMiddleware

app = FastAPI(docs_url='/api/docs' if not config['PROD'] else None,
              redoc_url='/api/redoc' if not config['PROD'] else None,
              openapi_url='/api/openapi.json' if not config['PROD'] else None)

POSTGRES_SQL_URL = config['POSTGRES_SQL_URL']

app.add_middleware(DBSessionMiddleware, db_url=POSTGRES_SQL_URL)

for file in os.listdir("routes"):
    if not file.startswith('_'):
        module_name, _ = os.path.splitext(file)
        module = __import__(f"routes.{module_name}", fromlist=[module_name])
        app.include_router(module.router, prefix=f"/api/{module_name}")


if __name__ == "__main__":
    configs = {
        'host': config['HOST'],
        'port': config['PORT'],
        'reload': not config['PROD'],
        'workers': config['workers'] if config['PROD'] else 1
    }
    uvicorn.run("app:app", **configs)

__all__ = ["app"]