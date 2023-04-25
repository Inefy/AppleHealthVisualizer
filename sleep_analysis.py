import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import seaborn as sns

def get_sleep_records_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    records = []

    # Extract sleep records from XML
    for record in root.findall('.//Record'):
        records.append(record.attrib)

    data = pd.DataFrame(records)
    return data

def preprocess_sleep_data(data):
    # Filter sleep data and convert date columns
    data['type'] = data['type'].astype(str)
    sleep_data = data[data['type'] == 'HKCategoryTypeIdentifierSleepAnalysis']
    sleep_data['startDate'] = pd.to_datetime(sleep_data['startDate'])
    sleep_data['endDate'] = pd.to_datetime(sleep_data['endDate'])

    return sleep_data

def analyze_sleep_data(sleep_data):
    # Extract total sleep, REM sleep, and deep sleep data
    total_sleep_data = sleep_data[sleep_data['value'] == 'HKCategoryValueSleepAnalysisAsleepUnspecified']
    rem_sleep_data = sleep_data[sleep_data['value'] == 'HKCategoryValueSleepAnalysisAsleepREM']
    deep_sleep_data = sleep_data[sleep_data['value'] == 'HKCategoryValueSleepAnalysisAsleepCore']

    # Calculate duration for each sleep type
    total_sleep_data['duration'] = total_sleep_data['endDate'] - total_sleep_data['startDate']
    rem_sleep_data['duration'] = rem_sleep_data['endDate'] - rem_sleep_data['startDate']
    deep_sleep_data['duration'] = deep_sleep_data['endDate'] - deep_sleep_data['startDate']

    # Group sleep data by date
    total_sleep = total_sleep_data.groupby(total_sleep_data['startDate'].dt.date)['duration'].sum()
    rem_sleep = rem_sleep_data.groupby(rem_sleep_data['startDate'].dt.date)['duration'].sum()
    deep_sleep = deep_sleep_data.groupby(deep_sleep_data['startDate'].dt.date)['duration'].sum()

    return total_sleep, rem_sleep, deep_sleep

def visualize_sleep_data(total_sleep, rem_sleep, deep_sleep):
    # Convert sleep duration to hours
    total_sleep = total_sleep.dt.total_seconds() / 3600
    rem_sleep = rem_sleep.dt.total_seconds() / 3600
    deep_sleep = deep_sleep.dt.total_seconds() / 3600

    # Set Seaborn style
    sns.set_style("whitegrid")

    # Create the plot
    plt.figure(figsize=(15, 5))

    # Plot sleep data
    sns.barplot(x=total_sleep.index, y=total_sleep.values, color='#4cc9f0', label='Light Sleep')
    sns.barplot(x=deep_sleep.index, y=deep_sleep.values, color='#4361ee', label='Deep Sleep')
    sns.barplot(x=rem_sleep.index, y=rem_sleep.values, color='#3f37c9', label='REM Sleep')

    # Set title and labels
    plt.title('Daily Sleep Duration', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sleep Duration (hours)', fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Add legend
    plt.legend()

    # Add statistics annotations
    for i, sleep_data in enumerate([total_sleep, deep_sleep, rem_sleep]):
        mean = sleep_data.mean()
        median = sleep_data.median()
        mode = sleep_data.mode().get(0, 'No mode')
        sleep_type = ['Light Sleep', 'Deep Sleep', 'REM Sleep'][i]
        stats_text = f'{sleep_type}\nMean: {mean:.2f}h\nMedian: {median:.2f}h\nMode: {mode:.2f}h' if mode != 'No mode' else f'{sleep_type}\nMean: {mean:.2f}h\nMedian: {median:.2f}h\nMode: {mode}'
        plt.annotate(stats_text, xy=(1.01, 0.65 - 0.25 * i), xycoords='axes fraction',
                     fontsize=10, fontweight='bold', color=['#4cc9f0', '#4361ee', '#3f37c9'][i])

    # Show the plot
    plt.show()

# Example usage:
# data = get_sleep_records_from_xml('path/to/xml/file.xml')
# sleep_data = preprocess_sleep_data(data)
# total_sleep, rem_sleep, deep_sleep = analyze_sleep_data(sleep_data)
# visualize_sleep_data(total_sleep, rem_sleep, deep_sleep)
