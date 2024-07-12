from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from db.database import database  # Correct import
from routers import data_collection

app = FastAPI(
    title="FastAPI Data Collector",
    description="API for collecting data from various regions",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "you@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(data_collection.router, prefix="/data", tags=["data collection"])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI Data Collector",
        version="1.0.0",
        description="API for collecting data from various regions",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://your-logo-url.com/logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
