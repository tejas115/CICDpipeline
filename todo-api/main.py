# main.py
from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response
import time

app = FastAPI()
hits = Counter("hits", "Number of hits to the root")
request_duration = Histogram("http_request_duration_seconds", "HTTP request duration in seconds", ["method", "endpoint"])

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    # Record metrics
    request_duration.labels(method=request.method, endpoint=request.url.path).observe(process_time)
    
    return response

@app.get("/")
def read_root():
    hits.inc()
    # return {"message": "Hello World"}
    # return {"message": f"Hello from CI/CD Pipeline! 🚀 Hits: {hits._value.get()}"} #changed API response from default. 
    # return {"message": f"🚀 FINAL TEST - CI/CD COMPLETE! Hits: {hits._value.get()}"}
    return {"message": f"🚀 PRODUCTION CI/CD PIPELINE! Hits: {hits._value.get()}"}
    # return {"message": f"🎯 LIVE INTERVIEW DEMO! Hits: {hits._value.get()}"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
