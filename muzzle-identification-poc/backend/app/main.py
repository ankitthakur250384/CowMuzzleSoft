from fastapi import FastAPI
from .api import routes

app = FastAPI(title="Muzzle Identification API")
app.include_router(routes.router)

@app.get('/')
def read_root():
    return {"status": "ok"}
