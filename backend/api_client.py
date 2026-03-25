import requests
import pickle
import os
import urllib.parse
from config import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COOKIE_PATH = os.path.join(BASE_DIR, "cookies.pkl")

BASE_URL = "https://payroll.razorpay.com"


def load_session():
    session = requests.Session()

    try:
        if not os.path.exists(COOKIE_PATH):
            print("❌ cookies.pkl not found")
            return None

        cookies = pickle.load(open(COOKIE_PATH, "rb"))

        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])

        return session

    except Exception as e:
        print("❌ Cookie load failed:", e)
        return None


def get_xsrf_token(session):
    for cookie in session.cookies:
        if cookie.name == "XSRF-TOKEN":
            return urllib.parse.unquote(cookie.value)  
    return None


def build_headers(xsrf_token):
    return {
        "X-XSRF-TOKEN": xsrf_token,
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": f"{BASE_URL}/dashboard"
    }

def check_in():
    session = load_session()
    if not session:
        return {"status": "error", "message": "Session not found. Run login again."}

    if not settings.LOCATION:
        return {"status": "error", "message": "Location not set in .env"}

    xsrf = get_xsrf_token(session)
    if not xsrf:
        return {"status": "error", "message": "XSRF token missing"}

    headers = build_headers(xsrf)

    payload = {"location": settings.LOCATION}

    try:
        res = session.post(
            f"{BASE_URL}/v2/api/attendance/check-in",
            json=payload,
            headers=headers
        )

        return {
            "status": "success" if res.status_code == 200 else "error",
            "code": res.status_code,
            "response": res.json()
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

def check_out():
    session = load_session()
    if not session:
        return {"status": "error", "message": "Session not found. Run login again."}

    if not settings.LOCATION:
        return {"status": "error", "message": "Location not set in .env"}

    xsrf = get_xsrf_token(session)
    if not xsrf:
        return {"status": "error", "message": "XSRF token missing"}

    headers = build_headers(xsrf)

    payload = {"location": settings.LOCATION}

    try:
        res = session.post(
            f"{BASE_URL}/v2/api/attendance/check-out",
            json=payload,
            headers=headers
        )

        return {
            "status": "success" if res.status_code == 200 else "error",
            "code": res.status_code,
            "response": res.json()
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_today_status(user_id):
    session = load_session()
    if not session:
        return {"status": "error", "message": "Session not found"}

    try:
        res = session.get(
            f"{BASE_URL}/v2/api/attendance/today?user_id={user_id}"
        )

        return {
            "status": "success" if res.status_code == 200 else "error",
            "code": res.status_code,
            "response": res.json()
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}