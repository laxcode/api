from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def add(a,b):
    return a+b

print(add(3,4))