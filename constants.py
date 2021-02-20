VULTR_URL = "https://www.vultr.com/products/cloud-compute/#pricing"

itens_base = "./div[{}]/span/strong/text()".format
VULTR_XPATHS = {
    'table': "//div[contains(@class, 'js-body')]",
    'rows': "./div//div[contains(@class, 'row-content')]",
    'storage': itens_base(2),
    'cpu': itens_base(3),
    'memory': "./div[4]/strong/text()",
    'bandwith': itens_base(5),
    'price': "./div[6]/span//text()"
}