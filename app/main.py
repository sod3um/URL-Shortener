from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
import uvicorn
import sqlite3
import validators

import database, utils #local
from schemas import Link, ShortCode #local

app = FastAPI()

@app.get("/")
def root():
    return {
        "name": "URL-Shortener",
        "version": "1.0-beta",
        "author": "sod3um",
        "docs": "/docs"
        }

@app.get("/{code}")
def click_handler(code: str, db: sqlite3.Connection = Depends(database.get_db)):
    row = db.execute("SELECT original_url FROM links WHERE short_code = ?", (code,)).fetchone()
    if row:
        return RedirectResponse(row['original_url'])

    return {
        "status": "404",
        "info": "Short code is not correct!"
        }

@app.post("/api/create")
def create_link(data: Link, db: sqlite3.Connection = Depends(database.get_db)):
    if not validators.url(data.url):
        return {
            "status": 400,
            "info": "Incorrect url format!"
        }
    row = utils.url_exist(data.url)
    if row:
        return {
            "status": 403,
            "info": "This link is already shortened!",
            "link": utils.create_link(row['short_code'])
        }

    short_code = utils.generate_short_code()
    db.execute("INSERT INTO links (original_url, short_code) VALUES (?, ?)", (data.url, short_code))
    db.commit()
    return {
        "status": 200,
        "info": "Link is successfully created!",
        "link": utils.create_link(short_code)
    }

if __name__ == "__main__":
    database.init_db()
    uvicorn.run(app, host=utils.HOST, port=utils.PORT)