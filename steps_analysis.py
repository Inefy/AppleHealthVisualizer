import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess_steps_data(data):
    # Filter steps data and convert columns to appropriate data types
    steps_data = data[data['type'] == 'HKQuantityTypeIdentifierStepCount']
    steps_data['startDate'] = pd.to_datetime(steps_data['startDate'])
    steps_data['endDate'] = pd.to_datetime(steps_data['endDate'])
    steps_data['value'] = pd.to_numeric(steps_data['value'])

    # Split the data into Apple Watch and iPhone data
    apple_watch_data = steps_data[steps_data['sourceName'].str.contains("Apple Watch")]
    iphone_data = steps_data[steps_data['sourceName'].str.contains("Da Phone")]

    # Iterate through iPhone data and remove rows with overlapping time periods in Apple Watch data
    iphone_data = iphone_data[~iphone_data.apply(lambda row: any((row['startDate'] <= apple_watch_data['endDate']) & (row['endDate'] >= apple_watch_data['startDate'])), axis=1)]

    # Combine the filtered Apple Watch and iPhone data
    steps_data = pd.concat([apple_watch_data, iphone_data])

    return steps_data


    return steps_data

def analyze_steps_data(steps_data):
    # Calculate daily total steps
    daily_steps = steps_data.groupby(steps_data['startDate'].dt.date)['value'].sum()
    return daily_steps

def visualize_steps_data(daily_steps):
    # Set Seaborn style for the plot
    sns.set_style("whitegrid")

    # Create a new figure with the specified size
    plt.figure(figsize=(15, 5))

    # Draw a bar plot for the daily total steps
    sns.barplot(x=daily_steps.index, y=daily_steps.values, color='#3f37c9')

    # Set title and axis labels for the plot
    plt.title('Daily Total Steps', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Steps', fontsize=12)

    # Rotate x-axis labels to make them more readable
    plt.xticks(rotation=45)

    # Calculate the mean and range of steps values
    mean_steps = daily_steps.mean()
    steps_range = daily_steps.max() - daily_steps.min()

    # Add annotations for the mean and range of steps values
    plt.annotate(f'Mean: {mean_steps:.2f} steps', xy=(1.01, 0.75), xycoords='axes fraction', fontsize=12, fontweight='bold', color='#3f37c9')
    plt.annotate(f'Range: {steps_range:.2f} steps', xy=(1.01, 0.65), xycoords='axes fraction', fontsize=12, fontweight='bold', color='#3f37c9')

    # Display the plot
    plt.show()
