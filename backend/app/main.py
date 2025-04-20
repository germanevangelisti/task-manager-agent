from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import tasks, ai
from .database import engine
from .models import task

# Create database tables
task.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tasks.router)
app.include_router(ai.router) 