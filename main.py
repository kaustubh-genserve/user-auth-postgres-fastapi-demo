from fastapi import FastAPI, Depends, Header, HTTPException, status
from fastapi import FastAPI
from fastapi import FastAPI, Depends, Header, HTTPException, status
from sqlmodel import Session, SQLModel, create_engine, select
from typing import List, Optional
from models import User
from contextlib import asynccontextmanager
import uvicorn

# DATABASE URL (PostgreSQL)

DATABASE_URL = "postgresql://postgres:1027074@localhost:5432/testdb"
engine = create_engine(DATABASE_URL, echo=True)

# Static token for simplicity
STATIC_TOKEN = "7777777777"

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

# Auth dependency
def verify_token(authorization: Optional[str] = Header(None)):
    print(f"Authorization Header: {authorization}")
    if authorization != f"Bearer {STATIC_TOKEN}":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )

# Add a user
@app.post("/users/", status_code=201, dependencies=[Depends(verify_token)])
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

# List all users
@app.get("/users/", response_model=List[User])
def list_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users
    

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )