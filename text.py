import json
import logging
from pathlib import Path
from string import Template

import requests
from spintax import spintax

from config import PACKAGE_FOLDER, REFERALS_API_HOST, REFERALS_API_PORT


def get_texts_json() -> dict:
    path = Path(PACKAGE_FOLDER, 'texts.json')
    with open(path, 'rb') as file:
        texts_config = json.load(file)
        return texts_config


def get_referals_json() -> dict:
    response = get_referals_response()
    values = response.json()
    return values


def get_referals_response() -> requests.Response:
    response = None
    while response is None:
        try:
            response = requests.get(f'http://{REFERALS_API_HOST}:{REFERALS_API_PORT}/referals')
            return response
        except Exception as err:
            logging.exception(err)


class Text:
    text = ''
    spins = ''
    project = ''

    @property
    def link(self):
        return self._fix_link(self._link)

    def __init__(self, lang: str, link: str, project: str):
        self._link = link
        referals_json: dict = get_referals_json().get(project)
        if referals_json:
            self.project = project
            self.spins = referals_json.get('spins')
        texts_json: dict = get_texts_json().get(lang)
        if texts_json:
            self.text = texts_json

    def _fix_link(self, link: str):
        link = link if 'https://' in link or 'https://' in link else f'http://{link}'
        return link

    def get_text(self, allow_stickers: bool = True):
        spinned_text = spintax.spin(self.text)
        template = Template(spinned_text)
        message = template.substitute(
            {'spins': self.spins,
             'project': self.project,
             'link': self.link}
        )
        if not allow_stickers:
            message = message.replace('🔥', '')
            message = message.replace('➡️', '>>>')
            message = message.replace('⬅️', '<<<')
        return message
