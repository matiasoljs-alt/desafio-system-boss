from fastapi import FastAPI
from routers.user import router as user_router
from routers.note import router as notes_router
app = FastAPI()

app.include_router(user_router)
app.include_router(notes_router)
