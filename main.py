from fastapi import FastAPI

app = FastAPI()

drivers = ["Driver1", "Driver2", "Driver3"]

@app.get("/")
def home():
    return {"message": "Ride Matching System Running"}

@app.get("/match")
def match_driver():
    return {"assigned_driver": drivers[0]}
