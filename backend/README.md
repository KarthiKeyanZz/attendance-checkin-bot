# Razorpay Check-in Bot 🚀

> ⚠️ This is a fun project built for learning and automation purposes.

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/KarthiKeyanZz/attendance-checkin-bot.git
cd razorpay-checkin-bot/backend
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file inside `backend/`:

```env
EMAIL=your_email_here
PASSWORD=your_password_here
NAME=your_name
LOCATION=Latitude,Langutude
```

---

### 5. Run backend server

```bash
uvicorn main:app --reload --port 9000
```

---

### 6. Open application

Go to:

```
http://127.0.0.1:9000
```

---

## 🔐 First Time Login

* Click **Login**
* Complete CAPTCHA in the browser window
* Cookies will be saved automatically

---

## ▶️ Usage

* Click **Check In** or **Check Out**
* Automation will run using Selenium
* Status will be shown in UI

---

## 🌐 Supported Browser

* ✅ **Brave Browser (Chromium-based)**

> Make sure Brave is installed and the path is correctly set in the script:
>
> ```python
> BRAVE_PATH = "/usr/bin/brave-browser"
> ```

---

## 📁 Project Structure

```
backend/
├── main.py
├── selenium_bot.py
├── login_once.py
├── config.py
├── cookies.pkl
├── static/
│   ├── style.css
│   ├── script.js
├── templates/
│   └── index.html
```

---

## ⚠️ Notes

* Ensure Brave browser is installed
* Update `BRAVE_PATH` if your system path differs
* Re-run login if session expires

---

## ✅ Done

You’re all set!
