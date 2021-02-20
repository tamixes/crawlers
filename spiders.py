import requests
from lxml import html

import json
import logging

from constants import VULTR_URL, VULTR_XPATHS
from utils import find_term

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class VultrSpider:
    def __init__(self):
        self.html = html
        self.items = []

    def start_request(self):
        """Starts the request page."""
        logger.info('Starting vultr spider request')

        request = requests.get(VULTR_URL)
        self.html = html.fromstring(request.content)

    def get_items(self):
        table = self.html.xpath(VULTR_XPATHS['table'])[0]
        rows = table.xpath(VULTR_XPATHS['rows'])
        items = []

        for row in rows:
            price = row.xpath(VULTR_XPATHS['price'])
            price = find_term(r'(\D\d\D*\d+\/\w+)', "".join(price))

            self.items.append([
                ('storage', row.xpath(VULTR_XPATHS['storage'])[0]),
                ('cpu', row.xpath(VULTR_XPATHS['cpu'])[0]),
                ('memory', row.xpath(VULTR_XPATHS['memory'])[0]),
                ('bandwith', row.xpath(VULTR_XPATHS['bandwith'])[0]),
                ('price', price)
            ])

    def log_items(self):
        for item in self.items:
            logger.info('Item %d: %s', (self.items.index(item) + 1),  item)


if __name__ == '__main__':
    vultr = VultrSpider()
    vultr.start_request()
    vultr.get_items()
    vultr.log_items()
