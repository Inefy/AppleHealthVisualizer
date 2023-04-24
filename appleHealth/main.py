from sleep_analysis import read_data, preprocess_sleep_data, analyze_sleep_data, visualize_sleep_data
from heart_rate_analysis import preprocess_heart_rate_data, analyze_heart_rate_data, visualize_heart_rate_data
from steps_analysis import preprocess_steps_data, analyze_steps_data, visualize_steps_data

if __name__ == "__main__":
    file_path = "path/to/your/apple_watch_data.xml"
    raw_data = read_data(file_path)

    sleep_data = preprocess_sleep_data(raw_data)
    daily_sleep = analyze_sleep_data(sleep_data)
    visualize_sleep_data(daily_sleep)
    heart_rate_data = preprocess_heart_rate_data(raw_data)
    daily_heart_rate = analyze_heart_rate_data(heart_rate_data)
    visualize_heart_rate_data(daily_heart_rate)

    steps_data = preprocess_steps_data(raw_data)
    daily_steps = analyze_steps_data(steps_data)
    visualize_steps_data(daily_steps)
