from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from util import scrape_purport, summarize_text

app = FastAPI(title="Vedabase SB Purport Summarizer")

class VerseRequest(BaseModel):
    verse: str
    summarize: bool = True

@app.get("/")
def read_root():
    return {"message": "Welcome to the SB Purport API"}

@app.post("/get_purport/")
def get_purport(req: VerseRequest):
    purport = scrape_purport(req.verse)
    if not purport:
        raise HTTPException(status_code=404, detail="Purport not found.")
    
    if req.summarize:
        summary = summarize_text(purport)
        return {"verse": req.verse, "summary": summary}
    
    return {"verse": req.verse, "purport": purport}
