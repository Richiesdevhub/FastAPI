from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(
    title= "Choose Your Own Adventure Game API",
    description = "api to generate cool stories",
    version = "0.1.0",
    docs_url= "/docs",
    redoc_url="/redoc",
)

app. add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS, #anterior aceptabamos todo ->allow_origins=["*"],
    allow_credencials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def main():
#     print("Hello from techwithtim-fullstack-farm-backend!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.app", host="0.0.0.0", post=8000, reload=True)
