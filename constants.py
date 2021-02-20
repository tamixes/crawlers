VULTR_URL = "https://www.vultr.com/products/cloud-compute/#pricing"

itens_base = "./div[{}]/span/text()".format
VULTR_XPATHS = {
    'table': "//div[contains(@class, 'js-body')]",
    'row': "./div//div[contains(@class, 'row-content')]",
    'storage': "./div[2]/span/strong/text()",
    'cpu': itens_base(3),
    'memory': "./div[4]/strong",
    'bandwith': itens_base(5),
    'price': itens_base(6)
}