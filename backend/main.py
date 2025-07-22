from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Relay backend is running"}

@app.post("/route")
def route_ticket(ticket: dict):
    # Simulated routing logic
    return {"status": "routed", "department": "HR"}
