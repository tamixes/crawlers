# About this project:

This project extracts data from [Digital Ocean](https://www.digitalocean.com/pricing/#droplet) and [Vultr](https://www.vultr.com/products/cloud-compute/#pricing). And allows you to save this data in two differents formats (csv and json).
## Libs used:

* python 3.7
* requests
* lxml


# How to run this project:
## Installing requirements:

Install the requirements running:

```shell
    $ pip install -r requirements.txt 
```
## Running all steps:

The file `runspiders.py` executes all steps on the requirements. To execute run on the console:

```shell
    $ python runspiders.py
```

## Running separeted steps:

Steps availiable:
    
* --print **spider_name** 
* --save_json **spider_name** 
* --save_csv **spider_name** 

Spiders names:

* vultr
* digital

To run a specific spider and a specific action execute:

```
    $ python run.py --print digital --save_json digital
```

