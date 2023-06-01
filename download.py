import requests

def download_file(file):
    res = requests.get(f'http://reports.ieso.ca/public/RealtimeMktTotals/{file}')
    return res
