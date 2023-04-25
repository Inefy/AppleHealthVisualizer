import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    # Set Seaborn style
    sns.set_style("whitegrid")

    # Create the plot
    plt.figure(figsize=(15, 5))

    # Plot the daily average heart rate
    sns.lineplot(x=daily_heart_rate.index, y=daily_heart_rate.values, color='#3f37c9', linewidth=2.5)

    # Set title and labels
    plt.title('Daily Average Heart Rate', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Heart Rate (BPM)', fontsize=12)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Calculate mean and range
    mean_heart_rate = daily_heart_rate.mean()
    heart_rate_range = daily_heart_rate.max() - daily_heart_rate.min()

    # Add mean and range annotations
    plt.annotate(f'Mean: {mean_heart_rate:.2f} BPM', xy=(1.01, 0.75), xycoords='axes fraction', fontsize=12, fontweight='bold', color='#3f37c9')
    plt.annotate(f'Range: {heart_rate_range:.2f} BPM', xy=(1.01, 0.65), xycoords='axes fraction', fontsize=12, fontweight='bold', color='#3f37c9')

    # Show the plot
    plt.show()

