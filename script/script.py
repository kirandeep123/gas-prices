import requests 
import csv 
import pandas as pd
import os
import urllib


BASE_URL = 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHD{}.xls'
DATE_COLUMN_XLS = 'Back to Contents'
PRICE_COLUMN_XLS = 'Data 1: Henry Hub Natural Gas Spot Price (Dollars per Million Btu)'
PRICE_COLUMN_WEEKLY_XLS = 'Data 1: Weekly Henry Hub Natural Gas Spot Price (Dollars per Million Btu)'

_dir_xls = "../data/xls/"
_dir_csv ="../data/csv/"

def download_file(url,item):
	if item=='d':
		urllib.request.urlretrieve(url, _dir_xls+'daily.xls')
	elif item=='w':
		urllib.request.urlretrieve(url, _dir_xls+'weekly.xls')
	elif item=='m':
		urllib.request.urlretrieve(url, _dir_xls+ 'monthly.xls')
	else:
		urllib.request.urlretrieve(url, _dir_xls +'annual.xls')

def make_directory(path):
	try:
		os.mkdir(path)
	except:
		return False
	return True



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
	 data_xls = pd.read_excel(_dir_xls +item+'.xls', 'Data 1')
	 data_xls['Date']= data_xls[DATE_COLUMN_XLS]
	 if item=='weekly':
		 data_xls['Price']= data_xls[PRICE_COLUMN_WEEKLY_XLS]
	 else:
		 data_xls['Price']= data_xls[PRICE_COLUMN_XLS]

	 data_xls = data_xls[['Date', 'Price']].iloc[2:].set_index(['Date'])
	 
	 if item=='monthly':
		 data_xls = normalize_df_date(data_xls)

	 data_xls.to_csv(_dir_csv+item +'.csv')
	 return data_xls

def normalize_df_date(df):
    df.index = df.index.map(lambda t: t.replace(day=1))
    return df

def main():	
	make_directory(_dir_csv)
	make_directory(_dir_xls)
	map ={
		'd':'daily',
		'w':'weekly',
		'm':'monthly',
		'y':'annual'
	}
	for item in map:
		urls = get_urls(item)
		download_file(urls, item)
		convert_to_csv(map[item])	
		
main()
