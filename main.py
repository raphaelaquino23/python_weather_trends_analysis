import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def get_dataset():
    data = pd.read_csv('DailyDelhiClimateTest.csv')
    return data

def display_climate(data):
    print('DATA HEAD')
    print(data.head())
    print('DESCRIBE')
    print(data.describe())
    print('DATA INFO')
    print(data.info())

def show_figure(figure):
    figure.show()

def get_figure(data, x, y, title):
    figure = px.line(data, x=x, y=y, title=title)
    return figure

def get_scatter_figure(data, x, y, size, trendline, title):
    figure = px.scatter(data_frame=data, x=x, y=y, size=size, trendline=trendline, title=title)
    return figure

if __name__ == '__main__':
    data = get_dataset()
    display_climate(data)
    meantemp_figure = get_figure(data, "date", "meantemp", "Mean Temperature of Delhi 2013-2017")
    humidity_figure = get_figure(data, "date", "humidity", "Humidity of Delhi 2013-2017")
    windspeed_figure = get_figure(data, "date", "wind_speed", "Wind Speed of Delhi 2013-2017")
    temp_humidity_scatter_figure = get_scatter_figure(data, "humidity", "meantemp", "meantemp", "ols","Relationship Between Humidity and Temperatore of Delhi 2013-2017")
    show_figure(meantemp_figure)
    show_figure(humidity_figure)
    show_figure(windspeed_figure)
    show_figure(temp_humidity_scatter_figure)

