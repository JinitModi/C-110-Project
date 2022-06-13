from cv2 import goodFeaturesToTrack
import random
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics

df= pd.read_csv('medium_data.csv')
data=df['title'].tolist()

def random_means(counter):
    dataframe=[]
    
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataframe.append(value)
    mean=statistics.mean(dataframe)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_displot([df], ["title"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0,1], mode="lines", name="mean"))
    fig.show()

def setup():
     mean_list=[]
     for i in range(0,1000):
        set_of_means = random_means(100)
        mean_list.append(set_of_means)

def mean_list():
    show_fig(mean_list)
    mean = statistics.mean(mean_list)