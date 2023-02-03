import json
from pathlib import Path
from string import Template

from spintax import spintax

from .config import PACKAGE_FOLDER


def get_texts() -> dict:
    path = Path(PACKAGE_FOLDER, 'texts.json')
    with open(path, 'rb') as file:
        texts_config = json.load(file)
        return texts_config


class Text:

    @property
    def link(self):
        return self._fix_link(self._link)

    def __init__(self, lang: str, link: str, project: str):
        json_file = get_texts()
        self._link = link
        self.project = project
        self.spins = json_file.get('spins').get(project)
        self.text = json_file.get('texts').get(lang)

    def _fix_link(self, link: str):
        link = link if 'https://' in link or 'https://' in link else f'http://{link}'
        return link

    def get_text(self, allow_stickers: bool = True):
        spinned_text = spintax.spin(self.text)
        template = Template(spinned_text)
        message = template.substitute(
            {'spins': self.spins,
             'project': self.project.capitalize(),
             'link': self.link}
        )
        if not allow_stickers:
            message = message.replace('🔥', '')
            message = message.replace('➡️', '>>>')
            message = message.replace('⬅️', '<<<')
        return message
