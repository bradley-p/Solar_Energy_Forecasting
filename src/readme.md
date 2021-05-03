## Contents

data_curating.ipynb - loads, cleans, and merges solar, weather, and astral

seasonal_learning.ipynb - splits data into warm (April - September) and cold (October - March) seasons and fits RF to each __Best Results__

learning_experiments.ipynb - fits various models to whole data set 

score_regression.py - uses sklearn metrics to evaluate model

visualization.ipynb - has code to make a few visualizations used in various presentations

hourly_averages.py - computes a rolling average (of a particular hour) and adds it to the .csv file. _note:_ averages did not improve performance in my experiments. 

data_functions.py - a small wrapper to make using Astral package easier for Logan, UT