# Solar Energy Forecasting
For powerpoint presentations see: <a href="https://github.com/bradley-p/Solar_Energy_Forecasting/blob/main/Reports:Notes/" >Reports Folder </a>

## Problem Statement: 
Predict the amount of energy produced by a grid of solar panels in the next hour given the current weather using machine learning methods.
## Motivation: 
There is a need to transition to green energy to prevent and reverse global climate change. Solar energy sources are a way to supplement energy needs in a clean way. The issue with solar energy is that energy production is dependent on weather conditions and varies throughout the day. If we can predict how much solar energy will be produced, we can modify the traditional power plants to accommodate the fluctuations in solar power. By producing less traditional energy during peak solar hours, we can reduce carbon emissions.
## Data:
The energy production of the solar panels maintained by Aspire labs is constantly monitored. They began collecting data in July 2019 and have provided me that data for this project. 
<p align="center">
<img width='350' height='250' src='images/Power_Generation_Fluctuates.png'>
</p>

The USU climate center keeps a detailed record of historically observed weather and is publicaly available. The input data was also supplemented by the Azimuth and Elevation angles of the sun at each timestep. These angles were calculated using the <a href='https://github.com/bradley-p/Solar_Energy_Forecasting/tree/main/src'>Astral</a> package 

## Methods:
A variety of Machine learning approaches have been applied. The results can be found in the <a href='https://github.com/bradley-p/Solar_Energy_Forecasting/tree/main/src'> src</a> folder
## Results: 




