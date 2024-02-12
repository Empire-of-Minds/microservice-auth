from __future__ import annotations

import os

from yaml import safe_load
import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()


# ? OpenAPI docs
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Microservice Auth API",
        version="1.0.0",
        summary="Microservice Auth API - OpenAPI schema",
        description="This is the OpenAPI schema for the Microservice Auth API",
        contact={"name": "Empire of Minds", "email": "empire.of.minds@gmail.com"},
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://raw.githubusercontent.com/Empire-of-Minds/microservice-auth/main/docs/pictures/microservice-auth_logo_bg-grey.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=bool(os.getenv("RELOAD_ENABLED", False)),
        use_colors=True,
        log_level="debug",
        log_config=safe_load("./storage/config/logging.yml"),
    )
