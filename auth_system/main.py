from fastapi import FastAPI
from database.connection import engine, Base
from routers import auth, user, profile

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Authentication & Profile System API", version="1.0")

# Include Routers
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(profile.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Mid-Level Auth System API. Go to /docs for Swagger UI."}