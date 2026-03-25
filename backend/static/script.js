const BASE_URL = "";

function setStatus(msg) {
    document.getElementById("status").innerText = msg;
}


async function login() {
    try {
        setStatus("Opening login... Please complete CAPTCHA");

        const res = await fetch(`${BASE_URL}/login`, {
            method: "POST"
        });

        const data = await res.json();
        console.log("Login response:", data);

        if (data.status === "success") {
            setStatus("Login successful ✅");

            await loadUser(); 

        } else {
            setStatus("Login failed ❌");
            alert("Login failed: " + data.message);
        }

    } catch (error) {
        console.error("Login error:", error);
        setStatus("Login error ❌");
    }
}

async function loadUser() {
    try {
        const res = await fetch(`${BASE_URL}/user`);
        const data = await res.json();

        console.log("User data:", data);

    
        document.getElementById("username").innerText =
            `Welcome, ${data.name} 👋`;

        document.getElementById("login-section").style.display = "none";
        document.getElementById("action-section").style.display = "block";

    } catch (error) {
        console.error("User fetch error:", error);
        setStatus("Failed to load user ❌");
    }
}

async function checkIn() {
    try {
        setStatus("Checking in...");

        const res = await fetch(`${BASE_URL}/checkin`, {
            method: "POST"
        });

        const data = await res.json();
        console.log("Check-in:", data);

        handleResponse(data);

    } catch (error) {
        console.error("Check-in error:", error);
        setStatus("Check-in failed ❌");
    }
}

async function checkOut() {
    try {
        setStatus("Checking out...");

        const res = await fetch(`${BASE_URL}/checkout`, {
            method: "POST"
        });

        const data = await res.json();
        console.log("Check-out:", data);

        handleResponse(data);

    } catch (error) {
        console.error("Check-out error:", error);
        setStatus("Check-out failed ❌");
    }
}


function handleResponse(data) {
    if (data.status === "success") {
        alert("✅ " + data.message);
        setStatus(data.message);
    } else {
        alert("❌ " + data.message);
        setStatus(data.message);
    }
}

async function testUser() {
    const res = await fetch(`${BASE_URL}/user`);
    const data = await res.json();

    console.log("Test User:", data);

    document.getElementById("username").innerText =
        `Welcome, ${data.name} 👋`;
}