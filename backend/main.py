# backend/main.py
from fastapi import FastAPI

# 1️⃣ Create a FastAPI app instance
app = FastAPI()

# 2️⃣ Define a basic route (GET request)
@app.get("/")
def home():
    return {"message": "Career Twin AI Backend is running 🚀"}

# 3️⃣ Define a test API endpoint (POST request)
@app.post("/simulate")
def simulate_career(age: int, education: str, goal: str):
    # Temporary mock logic for testing
    return {
        "career_path": goal,
        "predicted_salary": "₹15,00,000 / year",
        "stress_level": "6/10",
        "growth_curve": "medium",
        "message": f"Simulation for {education} at age {age} is ready."
    }
