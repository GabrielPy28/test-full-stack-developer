from fastapi import FastAPI
from api.v1.users.users import users_router
from api.v1.posts.posts import posts_router
from api.v1.photos.photos import photos_router
from api.v1.logs.logs import logs_router
import warnings
from fastapi.middleware.cors import CORSMiddleware

warnings.filterwarnings("ignore", message="Valid config keys have changed in V2:")

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(posts_router)
app.include_router(photos_router)
app.include_router(logs_router)

@app.get("/health")
def health():
    """Api health endpoint."""
    return {"Api is up and running"}