from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrase as wikiphrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "wikipedia API. call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search wikipedia"""

    results = search_wiki(value)
    return {"results": results}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Rerieve wikipedia page"""

    results = wikilogic(name)
    return {"results": results}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Rerieve wikipedia page and return phrases"""
    print(f"passed in name {name}")
    results = wikiphrases(name)
    print(f"results : {results}")
    return {"results": results}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
