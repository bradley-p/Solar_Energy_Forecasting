''' 
Add hourly averages of previous data.
Idea from one of the research papers
'''
import pandas as pd 
import numpy as np 
import datetime

filename = '/Users/brad/Desktop/CS6620/Project/Data/combined_processed_data1.csv' 
data = pd.read_csv(filename, sep=',')
data.drop('Unnamed: 0',axis=1, inplace=True)

# Use dictionary to keep track of hour averages and hour count
rolling_averages = {}
# avgs is the list of averages that will be appended to the dataframe 
avgs = []

for index, hour in enumerate(data['Hour']):
    # there is an existing rolling average for this hour
    if hour in rolling_averages:
        # we want the last average now so we don't include the answer 
        avgs.append(rolling_averages[hour])

        new_avg = (rolling_averages[hour]*rolling_averages[f'{hour}_count'] + data['Solar_average'][index])/(rolling_averages[f'{hour}_count'] + 1)
        rolling_averages[f'{hour}_count'] = rolling_averages[f'{hour}_count'] + 1
        rolling_averages[hour] = new_avg

    else:
        rolling_averages[hour] = data['Solar_average'][index]
        rolling_averages[f'{hour}_count'] = 1
        avgs.append(0)

if len(avgs) == len(data):
    print("The length matches! Merging new column now")
    data['Rolling_averages'] = avgs
    fname = '/Users/brad/Desktop/CS6620/Project/Data/combined_processed_data1.csv'
    data.to_csv(fname)
    print("New csv file saved!")
else:
    print(f'Length of avgs: {len(avgs)}, Length of data: {len(data)} \n No match :(')