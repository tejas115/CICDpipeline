# main.py
from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from starlette.responses import Response

app = FastAPI()
hits = Counter("hits", "Number of hits to the root")

@app.get("/")
def read_root():
    hits.inc()
    # return {"message": "Hello World"}
    # return {"message": f"Hello from CI/CD Pipeline! 🚀 Hits: {hits._value.get()}"} #changed API response from default. 
    # return {"message": f"🚀 FINAL TEST - CI/CD COMPLETE! Hits: {hits._value.get()}"}
    # return {"message": f"🚀 PRODUCTION CI/CD PIPELINE! Hits: {hits._value.get()}"}
    return {"message": f"🎯 LIVE INTERVIEW DEMO! Hits: {hits._value.get()}"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
