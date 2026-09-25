# FastAPI application entry point
from fastapi import FastAPI
from .api import regulation, user, notification

app = FastAPI(title="Agricultural Regulation Management API")

# Include routers
app.include_router(regulation.router, prefix="/regulations", tags=["regulations"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(notification.router, prefix="/notifications", tags=["notifications"])

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}
