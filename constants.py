VULTR_URL = "https://www.vultr.com/products/cloud-compute/#pricing"

vultr_items_base = "./div[{}]/span/strong/text()".format
VULTR_XPATHS = {
    "table": "//div[contains(@class, 'js-body')]",
    "rows": "./div//div[contains(@class, 'row-content')]",
    "storage": vultr_items_base(2),
    "cpu": vultr_items_base(3),
    "memory": "./div[4]/strong/text()",
    "bandwith": vultr_items_base(5),
    "price": "./div[6]/span//text()"
}

DIGITAL_URL = "https://www.digitalocean.com/pricing/#droplet"

digital_items_base = "./td[{}]/text()".format
DIGITAL_XPATHS = {
    "table": "//div[contains(@id, 'basic-droplets')]/following-sibling::table",
    "rows": "./tbody/tr",
    "memory": digital_items_base(1),
    "cpu": digital_items_base(2),
    "transfer": digital_items_base(3),
    "disk": digital_items_base(4),
    "hour_price": digital_items_base(5),
    "month_price": digital_items_base(6)
}
