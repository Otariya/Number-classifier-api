from fastapi import FastAPI

app = FastAPI()  # ✅ Ensure this exists

@app.get("/")
def read_root():
    return {"message": "Welcome to the Number Classification API"}
