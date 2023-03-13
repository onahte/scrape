
import requests
from config import FILE_SAVE_DESTINATIONDESTINATION

target = 'http://gaia.cs.umass.edu/wireshark-labs/alice.txt'
html = requests.get(target)
html_text = html.text

file_name = 'alice.txt'
with open(FILE_SAVE_DESTINATIONDESTINATIONDESTINATION + file_name, 'w') as f:
    f.write(html_text)
