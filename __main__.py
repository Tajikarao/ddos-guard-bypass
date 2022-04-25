import requests
import re

session = requests.Session()


def requests_ddos_guard(url):
    check = session.get("https://check.ddos-guard.net/check.js", headers={'referer': 'https://anidex.info/'}).text
    src = re.compile(r"new Image\(\).src = '(.+?)';")
    src = src.search(check).group(1)
    src = f'https://anidex.info/{src[1:]}'

    check2 = session.get(src, headers={'referer': 'https://anidex.info/'}).text

    check3 = session.get('https://anidex.info/').text
    print(check)



if __name__ == '__main__':
     test = requests_ddos_guard("https://anidex.info/")#.text
    # print(test)
