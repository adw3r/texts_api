import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import JSONResponse

from config import HOST, PORT, DEBUG
from text import Text, get_texts_json

app = FastAPI()


@app.get('/')
async def get_root():
    return JSONResponse(content=get_texts_json())


@app.get('/text')
async def get_text(lang: str, link: str, refname: str, with_stickers: bool = True):
    text = Text(lang=lang, link=link, project=refname).get_text(with_stickers).encode()
    return HTMLResponse(content=text)


if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=DEBUG)
