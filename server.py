from fastapi import FastAPI
from routes.userRoutes import router as userRoutes
from database.db import database


app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    if database.is_connected:
        print("Db connected")
    else:
        print("Db not connected")
    
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(userRoutes, prefix="/api")