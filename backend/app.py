import os
from fastapi import FastAPI

app = FastAPI()

for file in os.listdir("routes"):
    if not file.startswith('_'):
        module_name, _ = os.path.splitext(file)
        module = __import__(f"routes.{module_name}", fromlist=[module_name])
        app.include_router(module.router, prefix=f"/api/{module_name}")

