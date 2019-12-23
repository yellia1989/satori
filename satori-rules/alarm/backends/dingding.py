# -*- coding: utf-8 -*-

# -- stdlib --
import json

# -- third party --
import requests

# -- own --
from backend import Backend
from utils import status2emoji

# -- code --
class DingdingBackend(Backend):
    def send(self, ev):
        url = self.conf.get('url')
        if not url:
            return

        title = '%s[P%s] %s\n' % (
            status2emoji(ev['status']),
            ev['level'],
            ev['title'])
        text = '%s\n%s' % (title, ev['text'])

        resp = requests.post(
            url,
            headers={'Content-Type': 'application/json'},
            timeout=10,
            data=json.dumps({
                "msgtype": "markdown",
                "markdown": {
                    "title": title,
                    "text": text
                }
            }),
        )

        if not resp.ok:
            raise Exception(resp.content)

        rst = resp.json()

        if rst['errcode'] != 0:
            raise Exception(rst['errmsg'])


EXPORT = DingdingBackend
