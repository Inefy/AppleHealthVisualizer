import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

def get_sleep_records_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    records = []

    for record in root.findall('.//Record'):
        records.append(record.attrib)

    data = pd.DataFrame(records)
    return data

def preprocess_sleep_data(data):
    data['type'] = data['type'].astype(str)
    sleep_data = data[data['type'] == 'HKCategoryTypeIdentifierSleepAnalysis']
    sleep_data = sleep_data[sleep_data['value'] == 'HKCategoryValueSleepAnalysisAsleepUnspecified']
    sleep_data['startDate'] = pd.to_datetime(sleep_data['startDate'])
    sleep_data['endDate'] = pd.to_datetime(sleep_data['endDate'])
    return sleep_data

def analyze_sleep_data(sleep_data):
    sleep_data['duration'] = sleep_data['endDate'] - sleep_data['startDate']
    daily_sleep = sleep_data.groupby(sleep_data['startDate'].dt.date)['duration'].sum()
    return daily_sleep

def visualize_sleep_data(daily_sleep):
    # Convert sleep duration to hours and minutes
    daily_sleep = daily_sleep.dt.total_seconds() / 3600
    daily_sleep.plot(kind='bar', figsize=(15, 5), title='Daily Sleep Duration')
    plt.xlabel('Date')
    plt.ylabel('Sleep Duration (hours)')
    plt.show()

