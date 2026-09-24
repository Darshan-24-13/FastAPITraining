from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"page":"Home"}
@app.get("/about")
def about():
    return {"page":"About","author":"Darshan"}
@app.get("/health")
def health():
    return {"status":"Healthy"}