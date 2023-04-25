import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import seaborn as sns

def preprocess_heart_rate_data(data):
    # Filter heart rate data and convert columns to appropriate data types
    heart_rate_data = data[data['type'] == 'HKQuantityTypeIdentifierHeartRate']
    heart_rate_data['startDate'] = pd.to_datetime(heart_rate_data['startDate'])
    heart_rate_data['endDate'] = pd.to_datetime(heart_rate_data['endDate'])
    heart_rate_data['value'] = pd.to_numeric(heart_rate_data['value'])
    return heart_rate_data

def analyze_heart_rate_data(heart_rate_data):
    # Calculate daily average heart rate
    daily_heart_rate = heart_rate_data.groupby(heart_rate_data['startDate'].dt.date)['value'].mean()
    return daily_heart_rate

def visualize_heart_rate_data(daily_heart_rate):
    # Set Seaborn style for the plot
    sns.set_style("whitegrid")

    # Create a new figure with the specified size
    plt.figure(figsize=(15, 5))

    # Draw a line plot for the daily average heart rate values
    sns.lineplot(x=daily_heart_rate.index, y=daily_heart_rate.values, color='#0c0c0d', linewidth=2)

    # Prepare a colormap and normalize the data
    cmap = plt.get_cmap("coolwarm")
    norm = plt.Normalize(daily_heart_rate.min(), daily_heart_rate.max())
    colors = cmap(norm(daily_heart_rate.values))

    # Add colored dots for each data point based on the gradient
    for date, value, color in zip(daily_heart_rate.index, daily_heart_rate.values, colors):
        plt.scatter(date, value, color=color, edgecolors='k', s=75)

    # Set title and axis labels for the plot
    plt.title('Daily Average Heart Rate', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Heart Rate (BPM)', fontsize=12)

    # Rotate x-axis labels to make them more readable
    plt.xticks(rotation=45)

    # Calculate the mean and range of heart rate values
    mean_heart_rate = daily_heart_rate.mean()
    heart_rate_range = daily_heart_rate.max() - daily_heart_rate.min()

    # Add annotations for the mean and range of heart rate values
    plt.annotate(f'Mean: {mean_heart_rate:.2f} BPM', xy=(1.01, 0.75), xycoords='axes fraction', fontsize=12, fontweight='bold', color='#3f37c9')
    plt.annotate(f'Range: {heart_rate_range:.2f} BPM', xy=(1.01, 0.65), xycoords='axes fraction', fontsize=12, fontweight='bold', color='#3f37c9')

    # Display the plot
    plt.show()
