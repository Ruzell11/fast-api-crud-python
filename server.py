from fastapi import FastAPI
from routes.user_routes import router as userRoutes


app = FastAPI()

app.include_router(userRoutes, prefix="/api")