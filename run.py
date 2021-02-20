import getopt
import sys

from spiders import DigitalOceanSpider, VultrSpider

argument_list = sys.argv[1:]
short_options = "ho:v"
long_options = ["print", "save_csv", "save_json"]

try:
    arguments, values = getopt.getopt(
        argument_list, short_options, long_options)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-p", "--print"):
        if('digital' in values):
            digital = DigitalOceanSpider()
            digital.start_request()
            digital.get_items()
            digital.log_items()
        if('vultr' in values):
            vultr = VultrSpider()
            vultr.start_request()
            vultr.get_items()
            vultr.log_items()
    if current_argument in ("--save_csv"):
        if('digital' in values):
            digital = DigitalOceanSpider()
            digital.start_request()
            digital.get_items()
            digital.save_as_csv()
        if('vultr' in values):
            vultr = VultrSpider()
            vultr.start_request()
            vultr.get_items()
            vultr.save_as_csv()
    if current_argument in ("--save_json"):
        if('digital' in values):
            digital = DigitalOceanSpider()
            digital.start_request()
            digital.get_items()
            digital.save_as_json()
        if('vultr' in values):
            vultr = VultrSpider()
            vultr.start_request()
            vultr.get_items()
            vultr.save_as_json()