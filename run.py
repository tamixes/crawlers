import getopt
import sys

from spiders import DigitalOceanSpider, VultrSpider
from utils import (save_csv,
                   save_json,
                   log_spider_items)

argument_list = sys.argv[1:]
short_options = "ho:v"
long_options = ["print", "save_csv", "save_json"]

digital = DigitalOceanSpider()
vultr = VultrSpider()


try:
    arguments, values = getopt.getopt(
        argument_list, short_options, long_options)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-p", "--print"):
        if('digital' in values):
            log_spider_items(digital)
        if('vultr' in values):
            log_spider_items(vultr)
    if current_argument in ("--save_csv"):
        if('digital' in values):
            save_csv(digital)
        if('vultr' in values):
            save_csv(vultr)
    if current_argument in ("--save_json"):
        if('digital' in values):
            save_json(digital)
        if('vultr' in values):
            save_json(vultr)
