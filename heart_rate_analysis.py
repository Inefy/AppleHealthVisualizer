import pandas as pd
import matplotlib.pyplot as plt

def preprocess_heart_rate_data(data):
    heart_rate_data = data[data['type'] == 'HKQuantityTypeIdentifierHeartRate']
    heart_rate_data['startDate'] = pd.to_datetime(heart_rate_data['startDate'])
    heart_rate_data['endDate'] = pd.to_datetime(heart_rate_data['endDate'])
    heart_rate_data['value'] = pd.to_numeric(heart_rate_data['value'])
    return heart_rate_data

def analyze_heart_rate_data(heart_rate_data):
    daily_heart_rate = heart_rate_data.groupby(heart_rate_data['startDate'].dt.date)['value'].mean()
    return daily_heart_rate

def visualize_heart_rate_data(daily_heart_rate):
    daily_heart_rate.plot(kind='line', figsize=(15, 5), title='Daily Average Heart Rate')
    plt.xlabel('Date')
    plt.ylabel('Heart Rate (BPM)')
    plt.show()
