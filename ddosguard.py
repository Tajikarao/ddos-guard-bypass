from urllib.parse import urlparse
import httpx
import re

class DDOSGuard():
    def __init__(self) -> None:
        self.endpoints = {
            "check": "https://check.ddos-guard.net/check.js"
        }

        self.session = httpx.Client(http2=True, headers={'user-agent': 'DDOS-GUARD Bypasser'})

    def get_check(self):
        return self.session.get(self.endpoints["check"]).text

    def parse_check(self, check):
        src = re.compile(r"new Image\(\).src = '(.+?)';")
        return src.search(check).group(1)

    def src_validator(self, domaine, src):
        self.session.get(f"{domaine}{src}")

    def parse_domaine(self, url):
        url_parse = urlparse(url)
        return f"{url_parse.scheme}://{url_parse.netloc}"

    
    def get(self, url, headers=None):
        parse_domaine = self.parse_domaine(url)

        check = self.get_check()
        parse_check = self.parse_check(check)

        self.src_validator(parse_domaine, parse_check)


        return self.session.get(url, headers=headers)
