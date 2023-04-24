import pandas as pd
import matplotlib.pyplot as plt

def preprocess_steps_data(data):
    steps_data = data[data['type'] == 'HKQuantityTypeIdentifierStepCount']
    steps_data['startDate'] = pd.to_datetime(steps_data['startDate'])
    steps_data['endDate'] = pd.to_datetime(steps_data['endDate'])
    steps_data['value'] = pd.to_numeric(steps_data['value'])
    return steps_data

def analyze_steps_data(steps_data):
    daily_steps = steps_data.groupby(steps_data['startDate'].dt.date)['value'].sum()
    return daily_steps

def visualize_steps_data(daily_steps):
    daily_steps.plot(kind='bar', figsize=(15, 5), title='Daily Steps Count')
    plt.xlabel('Date')
    plt.ylabel('Steps Count')
    plt.show()