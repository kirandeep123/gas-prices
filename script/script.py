import requests 
import csv 
import pandas as pd
import os
import urllib


HENRY_HUB_BASE_URL = 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHD{}.xls'
_dir = "./data/xls"
def download_file(url,item):
	if item=='d':
		urllib.request.urlretrieve(url, 'gas-prices/data/xls/daily.xls')
	elif item=='w':
		urllib.request.urlretrieve(url, 'gas-prices/data/xls/weekly.xls')
	elif item=='m':
		urllib.request.urlretrieve(url, 'gas-prices/data/xls/monthly.xls')
	else:
		urllib.request.urlretrieve(url, 'gas-prices/data/xls/yearly.xls')

def make_directory(path):
	os.mkdir(path)

	
def get_urls(duration):
	if duration=='d':
		return 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls'
	elif duration=='w' :
		return 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDw.xls'
	elif duration=='m' :
		return 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls'
	else:
		return 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDa.xls'
	
def convert_to_csv(item):	
	 data_xls = pd.read_excel('daily.xls', 'Data 1')
	 data_xls.to_csv(item +'.csv')

def main():	
	map ={
		'd':'daily',
		'w':'weekly',
		'm':'monthly',
		'y':'annual'
	}
	list = ['d','w','m','y']
	for item in list:
		urls = get_urls(item)
		download_file(urls, item)
		convert_to_csv(map[item])	
		
main()
