from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/mult")
def read_ops(op1, op2):
    if not op1 or not op2:
        return {'resultado' : "op1 ou op2 não foi informado"}

    return {'resultado' : float(op1) * float(op2)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)