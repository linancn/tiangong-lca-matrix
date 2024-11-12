from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.config.config import (
    FASTAPI_AUTH,
    FASTAPI_BEARER_TOKEN,
)

bearer_scheme = HTTPBearer()


def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if (
        credentials.scheme != "Bearer"
        or credentials.credentials != FASTAPI_BEARER_TOKEN
    ):
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return credentials


app = FastAPI(
    title="TianGong LCA Matrix API",
    version="1.0",
    description="TianGong LCA Matrix API Server",
    dependencies=[Depends(validate_token)] if FASTAPI_AUTH else None,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
