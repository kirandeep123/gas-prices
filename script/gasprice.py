import os
import requests
import pandas


CSV_FOLDER = './data/csv'
XLS_FOLDER = './data/xls'
TIME_FRAME = ['d', 'w', 'm', 'a']
NAME_MAP = {
    'd': 'daily',
    'w': 'weekly',
    'm': 'monthly',
    'a': 'annually'
}


'''
creates a data folder for both csv and xls files
'''
def make_data_folder():
    if not os.path.isdir(CSV_FOLDER):
        os.mkdir(CSV_FOLDER)
    if not os.path.isdir(XLS_FOLDER):    
        os.mkdir(XLS_FOLDER)
    return True


'''
get gas prices as per different time frames 
'''
def gas_prices_time_frame():
    for duration in TIME_FRAME:
        yield NAME_MAP[duration], 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHD' + duration + '.xls'


'''
download the xls files for all time frames
'''
def download_file(name, url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(XLS_FOLDER + '/' + name + '.xls', 'wb') as f:
            f.write(response.content)


'''
downloaded xls files are converted in csv files 
and stored in data folder respectively
'''
def convert_xls_to_csv(duration):        
    data_xls = pandas.read_excel(XLS_FOLDER + '/' + duration + '.xls', 'Data 1', index_col=None).iloc[2:]
    data_xls['Date'] = pandas.to_datetime(data_xls['Back to Contents']).dt.date
    
    if duration != 'weekly':
        data_xls['Price'] = data_xls['Data 1: Henry Hub Natural Gas Spot Price (Dollars per Million Btu)']
    else:
        data_xls['Price'] = data_xls['Data 1: Weekly Henry Hub Natural Gas Spot Price (Dollars per Million Btu)']
    data_xls.reset_index(drop=True, inplace=True)

    data_xls[['Date', 'Price']].to_csv(CSV_FOLDER + '/' + duration + '.csv', index=False)



def main():
    make_data_folder()
    for name, url in gas_prices_time_frame():
        download_file(name, url)
        convert_xls_to_csv(name)
    
if __name__ == "__main__":
    main()