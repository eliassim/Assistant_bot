import webbrowser
import requests
import bs4
import sys

res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))