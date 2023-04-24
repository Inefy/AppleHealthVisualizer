import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import numpy as np
import seaborn as sns

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
    # Convert sleep duration to hours
    daily_sleep = daily_sleep.dt.total_seconds() / 3600

    # Set Seaborn style and create color map
    sns.set_style("whitegrid")
    cmap = plt.get_cmap("coolwarm_r")
    norm = plt.Normalize(daily_sleep.min(), daily_sleep.max())
    
    # Create the plot
    plt.figure(figsize=(15, 5))
    sns.barplot(x=daily_sleep.index, y=daily_sleep.values, palette=cmap(norm(daily_sleep.values)))

    # Set title and labels
    plt.title('Daily Sleep Duration', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sleep Duration (hours)', fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()