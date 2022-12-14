from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import routers
from config import settings

app = FastAPI()

if len(settings.CORS_ORIGINS) > 0:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
routers.init_app(app)


@app.get("/")
def read_root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True)
