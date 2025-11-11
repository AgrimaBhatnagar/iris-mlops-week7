from fastapi import FastAPI
from app.schemas import IrisRequest, IrisResponse
from app.model import model

app = FastAPI(title="IRIS API")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/predict", response_model=IrisResponse)
def predict(req: IrisRequest):
    y = model.predict(req.X)
    return {"y": y}
