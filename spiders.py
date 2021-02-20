import requests
from lxml import html

import logging

from constants import VULTR_URL, VULTR_XPATHS, DIGITAL_URL, DIGITAL_XPATHS
from utils import find_term, log_items, save_as_json, save_as_csv

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
        log_items(self.items)

    def save_as_json(self):
       save_as_json('vults_items.json', self.items)

    def save_as_csv(self):
        fieldnames = ['storage', 'cpu', 'memory', 'bandwith', 'price']
        save_as_csv('vultr_items.csv', self.items, fieldnames)

class DigitalOceanSpider:
    def __init__(self):
        self.html = html
        self.items = []

    def start_request(self):
        """Starts the request page."""
        logger.info('Starting digital ocean spider request')

        request = requests.get(DIGITAL_URL)
        self.html = html.fromstring(request.content)


    def get_items(self):
        """Gets the page items."""
        table = self.html.xpath(DIGITAL_XPATHS['table'])[0]
        rows = table.xpath(DIGITAL_XPATHS['rows'])

        for row in rows:
            items = {
                'memory': row.xpath(DIGITAL_XPATHS['memory'])[0],
                'vCPUs': row.xpath(DIGITAL_XPATHS['cpu'])[0],
                'transfer': row.xpath(DIGITAL_XPATHS['transfer'])[0],
                'disk': row.xpath(DIGITAL_XPATHS['disk'])[0],
                'hour_price': row.xpath(DIGITAL_XPATHS['hour_price'])[0],
                'month_price': row.xpath(DIGITAL_XPATHS['month_price'])[0],
            }
            self.items.append(items)

    def log_items(self):
        log_items(self.items)

    def save_as_json(self):
        save_as_json('digital_items.json', self.items)

    def save_as_csv(self):
        fieldnames = ['memory', 'vCPUs', 'transfer', 'disk', 'hour_price', 'month_price']
        save_as_csv('digital_items.csv', self.items, fieldnames)
