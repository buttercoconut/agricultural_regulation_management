# FastAPI app
from fastapi import FastAPI
from .api import regulation, user, notification

app = FastAPI(title="Agricultural Regulation Management API")

app.include_router(regulation.router)
app.include_router(user.router)
app.include_router(notification.router)
