import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

from module.config import HOST, PORT
from module.text import Text

app = FastAPI()


@app.get('/')
async def get_root():
    return RedirectResponse('/docs')


@app.get('/text')
async def get_text(lang: str, link: str, refname: str, with_stickers: bool = True):
    text = Text(lang=lang, link=link, project=refname).get_text(with_stickers).encode()
    return HTMLResponse(content=text)


if __name__ == '__main__':
    uvicorn.run('main:app', host=HOST, port=int(PORT))
