import scrapy
from selenium import webdriver

class GooglePatentsSipder(scrapy.Spider):

    name = 'googleSpider'

    start_urls =["https://patents.google.com/?q=aloe+vera"]


