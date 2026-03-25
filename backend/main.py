from fastapi import FastAPI, Request
from config import settings

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

from login_once import save_login_session
from api_client import check_in, check_out, get_today_status
from selenium_bot import run_attendance

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def serve_ui():
    return FileResponse("templates/index.html")

@app.get("/user")
def get_user():
    return {
        "name": settings.NAME
    }

@app.get("/env")
def env_test():
    return {
        "email": settings.EMAIL,
        "location": settings.LOCATION
    }

@app.post("/login")
def login():
    try:
        save_login_session()
        return {"status": "success", "message": "Login completed & cookies saved"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/checkin")
def checkin():
    return run_attendance("checkin")

@app.post("/checkout")
def checkout():
    return run_attendance("checkout")

@app.get("/status")
def status():
    USER_ID = 1437269
    return get_today_status(user_id=USER_ID)