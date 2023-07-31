from fastapi import FastAPI
import uvicorn
from shit import da_shit
app = FastAPI()


@app.get("/")
def read_root():
    x = "debug"
    print(x)
    x = da_shit()
    return {"Hello": "1111", "shit": x}


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=80, reload=True)
