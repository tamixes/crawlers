import logging

from spiders import DigitalOceanSpider, VultrSpider
from utils import start_request

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class Runspiders:
    def __init__(self):
        self.vultr = VultrSpider()
        self.digital = DigitalOceanSpider()

    def first_step(self, spider, step):
        """Runs the first step (print all data).
        """
        logger.info("Executing %d step to %s", step, spider.__class__.__name__)
        start_request(spider)
        spider.log_items()

    def second_step(self, spider, step):
        """Runs the second step (print all data and save as json).
        """
        self.first_step(spider, step)
        spider.save_as_json()

    def third_step(self, spider, step):
        """Runs the third step (print all data, save as json and csv).
        """
        self.second_step(spider, step)
        spider.save_as_csv()

    def run_steps(self, spider):
        """Runs all three steps.
        """
        self.first_step(spider, 1)
        self.second_step(spider, 2)
        self.third_step(spider, 3)

    def run_spiders(self):
        """Calls run_steps to digital and vultr spiders.
        """
        self.run_steps(self.digital)
        self.run_steps(self.vultr)


if __name__ == '__main__':
    run_spider = Runspiders()
    run_spider.run_spiders()
