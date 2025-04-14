from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Modello per richiesta API
class RequestData(BaseModel):
    folder: str

@app.get("/")
def read_root():
    return {"message": "GPT OneDrive API is running ✅"}

@app.post("/files")
def read_files(data: RequestData):
    folder_path = data.folder
    # Simulazione: restituisce il percorso ricevuto (sostituisci con la tua logica)
    return {"received_folder": folder_path}

if __name__ == "__main__":
    # Porta dinamica per Render
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
