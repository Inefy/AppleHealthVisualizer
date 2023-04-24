import pandas as pd
import matplotlib.pyplot as plt
from lxml import etree

def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    root = etree.fromstring(content.encode('utf-8'))

    records = []
    for record in root.findall('.//Record'):
        attributes = record.attrib
        records.append(attributes)

    data = pd.DataFrame(records)
    return data

def preprocess_sleep_data(data):
    data['type'] = data['type'].astype(str)
    sleep_data = data[data['type'] == 'HKCategoryTypeIdentifierSleepAnalysis']
    sleep_data['startDate'] = pd.to_datetime(sleep_data['startDate'])
    sleep_data['endDate'] = pd.to_datetime(sleep_data['endDate'])
    return sleep_data

def analyze_sleep_data(sleep_data):
    sleep_data['duration'] = sleep_data['endDate'] - sleep_data['startDate']
    daily_sleep = sleep_data.groupby(sleep_data['startDate'].dt.date)['duration'].sum()
    return daily_sleep

def visualize_sleep_data(daily_sleep):
    daily_sleep.plot(kind='bar', figsize=(15, 5), title='Daily Sleep Duration')
    plt.xlabel('Date')
    plt.ylabel('Sleep Duration (seconds)')
    plt.show()