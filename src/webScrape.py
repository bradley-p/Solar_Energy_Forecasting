import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


# North Logan Green Canyon
#41.76553/-111.78895
Site = 'http://forecast.weather.gov/MapClick.php?w0=t&w3u=1&w4=sky&w5=pop&w7=rain&AheadHour=0&Submit=Submit&FcstType=digital&lat=41.76553&lon=-111.78895&site=all&unit=0&dd=&bw='


class scraper:

    def __init__(self):
        pass