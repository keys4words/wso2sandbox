from fastapi import FastAPI, Body
import uvicorn


app = FastAPI()


@app.get("/api/small")
async def small():
    return "Return string in 256 symbols"

@app.get("/api/middle")
async def middle():
    return "Return string in 1024 symbols"

@app.get("/api/big")
async def big():
    return "Return string in 16256 symbols"

@app.post("/api/hello")
async def hello(data=Body()):
    return f"I've got it: {data}"


if __name__ == '__main__':
    uvicorn.run("main:app", 
                host="0.0.0.0", 
                port=8000, 
                reload=True,
                )