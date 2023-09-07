from fastapi import FastAPI, BackgroundTasks
import uvicorn as uvicorn

from machine_request import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# Not sure how you want to handle the route and parsing of the data
@app.get("/machine/{building}/{roomNumber}/{machineType}/{machineNumber}/{problemDetail}")
async def demoOrder(BackgroundTasks: BackgroundTasks):
    report = MachineRequest("Gleason", "35-A079", "Washer", "17", "It seems that this machine is not receiving power")
    BackgroundTasks.add_task(api_request, report)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
