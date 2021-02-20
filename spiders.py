import requests
from lxml import html

from constants import VULTR_URL, VULTR_XPATHS

class VultrSpider:
    def start_request(self):
        request = requests.get(VULTR_URL)
        tree = html.fromstring(request.content)


if __name__ == '__main__':
    vultr = VultrSpider()
    vultr.start_request()