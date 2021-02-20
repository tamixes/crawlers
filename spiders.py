import requests
from lxml import html

import csv
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
        """Gets the page items."""
        table = self.html.xpath(VULTR_XPATHS['table'])[0]
        rows = table.xpath(VULTR_XPATHS['rows'])

        for row in rows:
            price = row.xpath(VULTR_XPATHS['price'])
            price = find_term(r'(\$+\d+\.?\d?\d*\/\w+)', "".join(price))

            items = {
                'storage': row.xpath(VULTR_XPATHS['storage'])[0],
                'cpu': row.xpath(VULTR_XPATHS['cpu'])[0],
                'memory': row.xpath(VULTR_XPATHS['memory'])[0],
                'bandwith': row.xpath(VULTR_XPATHS['bandwith'])[0],
                'price': price,
            }
            self.items.append(items)

    def log_items(self):
        """Log the items."""
        for item in self.items:
            logger.info('Item %d: %s', (self.items.index(item) + 1),  item)

    def save_as_json(self):
        """Save items as json file."""
        logger.info('Saving items as json.')

        with open('items.json', 'w') as items_json:
            json.dump(self.items, items_json, indent=4)

    def save_as_csv(self):
        """Save items as csv."""
        logger.info('Saving items as csv.')

        with open('items.csv', 'w') as items_csv:
            fieldnames = ['storage', 'cpu', 'memory', 'bandwith', 'price']
            writer = csv.DictWriter(items_csv, fieldnames)
            writer.writeheader()
            for item in self.items:
                writer.writerow(item)


if __name__ == '__main__':
    vultr = VultrSpider()
    vultr.start_request()
    vultr.get_items()

