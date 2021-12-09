from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import csv
import pandas as pd

URL = "https://en.wikipedia.org/wiki/Donald_Trump"
html_code = requests.get(URL)

soup = BeautifulSoup(html_code.content, 'html5lib')
soup2 = BeautifulSoup(html_code.text, "html.parser")
table_id = "infobox_vcard"
soup_table = soup.find('table', {'class':table_id})

trump_info = soup2.find("table", attrs={"id" : soup_table})

df = pd.read_html(str(trump_info))

title = soup.title

table_print = trump_info
table_pretty = table_print.prettify()

print(table_print.find_all('p'))

print("END")

