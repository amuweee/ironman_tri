import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None #remove chaining warning


class get_dataframes:

    # Initialize and import the whole race dataset as DataFrame
    def __init__(self):
        query = "SELECT * FROM ironman_race"
        c = sqlite3.connect('../../ironman.db')
        self.df = pd.read_sql_query(query, c)

    # Turn date into proper format, and add transition time column
    def add_transition_time(self):
        self.df['Time_Swim'] = pd.to_timedelta(self.df['Time_Swim'], errors='coerce')
        self.df['Time_Bike'] = pd.to_timedelta(self.df['Time_Bike'], errors='coerce')
        self.df['Time_Run'] = pd.to_timedelta(self.df['Time_Run'], errors='coerce')
        self.df['Time_Finish'] = pd.to_timedelta(self.df['Time_Finish'], errors='coerce')
        self.df['temp'] = self.df['Time_Finish'] - self.df['Time_Swim'] - self.df['Time_Bike'] - self.df['Time_Run']
        self.df['Time_Transition'] = np.where(self.df['Time_Finish'] == '00:00:00', self.df['Time_Finish'], self.df['temp'])
        self.df = self.df.drop('temp', 1)
        return self.df


"""
DNF / DNS Analysis
"""
