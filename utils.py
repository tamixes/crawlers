import csv
import json
import logging
import re

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def find_term(pattern, string, flags=0):
    """Returns a clean term based on the pattern received.
    """
    return re.findall(pattern, string, flags=flags)


def log_items(items):
    """Logs the items.
    """
    for item in items:
        logger.info('Item %d: %s', (items.index(item) + 1),  item)


def save_as_json(file_name, items):
    """Save items as json file.
    """
    logger.info('Saving items as json.')
    with open(file_name, 'w') as items_json:
        json.dump(items, items_json, indent=4)


def save_as_csv(file_name, items, fieldnames):
    """Save items as csv.
    """
    logger.info('Saving items as csv.')

    with open(file_name, 'w') as items_csv:
        writer = csv.DictWriter(items_csv, fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow(item)


def start_request(spider):
    """Starts the request and get the items from the page.
    """
    spider.start_request()
    spider.get_items()


def log_spider_items(spider):
    """Logs all items on the console.
    """
    start_request(spider)
    spider.log_items()


def save_json(spider):
    """Saves the items into a json file.
    """
    start_request(spider)
    spider.save_as_json()


def save_csv(spider):
    """Saves the items into a csv file.
    """
    start_request(spider)
    spider.save_as_csv()
