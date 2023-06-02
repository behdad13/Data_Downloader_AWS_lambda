import requests

# Change the website for your own use
def download_file(file):
    res = requests.get(f'http://reports.ieso.ca/public/RealtimeMktTotals/{file}')
    return res
