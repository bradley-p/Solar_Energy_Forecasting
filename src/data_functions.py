import numpy as np 
import astral
from astral import sun
import pytz
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

###
# File contains methods useful for curating data
# helps to clean-up the data curating notebook
# provides method that computes elevation, azimuth, and zenith using astral package
## 

def plotRegression(truth, pred):
    plt.figure(figsize=(10,10))
    plt.scatter(truth, pred)
    plt.grid()
    plt.xlabel("Truth")
    plt.ylabel("Predicted")
    plt.title("Truth Plotted against actual value")
    plt.plot([min(truth),max(truth)], [min(truth),max(truth)], 'r')
    plt.show()
    
def computeAverageError(pred, y):
    err = []
    for i in range(len(pred)):
        err.append(abs((y[i] - pred[i])/(y[i] + 1e-6)))

    return sum(err)/ len(err)

class LoganAstral:
    def __init__(self):
        #going to use these variables a lot 
        self.MST = pytz.timezone('US/Mountain')
        self.logan = astral.LocationInfo(name='Logan, UT', region='US/Mountain', timezone=self.MST, latitude=41.7452, longitude=-111.8097)
        self.observer = self.logan.observer

    # Astral expects UTC time. We are assuming input is in MST 
    def timeToUTC(self, mstDT):
        return self.MST.normalize(self.MST.localize(mstDT)).astimezone(pytz.utc)

    # computes the three 
    def computeElAzZe(self, dt):
        utcDT = self.timeToUTC(dt)
        elevation = sun.elevation(self.observer, utcDT)
        azimuth = sun.azimuth(self.observer, utcDT)
        zenith = sun.zenith(self.observer, utcDT)
        return (elevation, azimuth, zenith)


if __name__=='__main__':
    year = 2021
    month = 3
    day = 26
    hour = 7
    minutes = 19
    seconds = 0
    dt = datetime(year, month, day, hour, minutes, seconds)
    lat = 41.7452
    lon = -111.8097
    MST = pytz.timezone('US/Mountain')
    logan = astral.LocationInfo(name='Logan, UT', timezone=MST, latitude=lat, longitude=lon)
     # this is how to convert from local time to UTC, which astral expects 
    utcdt = MST.normalize(MST.localize(dt)).astimezone(pytz.utc)
    print(sun.zenith_and_azimuth(logan.observer, utcdt))
    print(sun.elevation(logan.observer, utcdt))
