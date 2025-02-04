from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.answer import answer_router
from domain.question import question_router
from fastapi.responses import PlainTextResponse

app = FastAPI()

origins = [
        "http://127.0.0.1:5173", "http://localhost:5173" , 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(question_router.router)
app.include_router(answer_router.router)

@app.get("/health")
async def health_check():
    return PlainTextResponse("건강합니다",status_code=200)
