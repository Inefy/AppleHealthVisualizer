from sleep_analysis import get_sleep_records_from_xml, preprocess_sleep_data, analyze_sleep_data, visualize_sleep_data
from heart_rate_analysis import preprocess_heart_rate_data, analyze_heart_rate_data, visualize_heart_rate_data
from steps_analysis import preprocess_steps_data, analyze_steps_data, visualize_steps_data

def get_data_range(data, start_date, end_date):
    return data[(data['startDate'] >= start_date) & (data['endDate'] <= end_date)]

if __name__ == "__main__":
    file_path = "/home/zacbatten/Documents/projects/appleHealth/apple_health_export/export.xml"
    raw_data = get_sleep_records_from_xml(file_path)

    data_type = input("Enter the data type you want to analyze (heart_rate, steps, sleep): ")
    start_date = input("Enter the start date for the data range (yyyy-mm-dd): ")
    end_date = input("Enter the end date for the data range (yyyy-mm-dd): ")

    if data_type.lower() == "sleep":
        sleep_data = preprocess_sleep_data(raw_data)
        sleep_data = get_data_range(sleep_data, start_date, end_date)
        daily_sleep = analyze_sleep_data(sleep_data)
        visualize_sleep_data(daily_sleep)

    elif data_type.lower() == "heart_rate":
        heart_rate_data = preprocess_heart_rate_data(raw_data)
        heart_rate_data = get_data_range(heart_rate_data, start_date, end_date)
        daily_heart_rate = analyze_heart_rate_data(heart_rate_data)
        visualize_heart_rate_data(daily_heart_rate)

    elif data_type.lower() == "steps":
        steps_data = preprocess_steps_data(raw_data)
        steps_data = get_data_range(steps_data, start_date, end_date)
        daily_steps = analyze_steps_data(steps_data)
        visualize_steps_data(daily_steps)

    else:
        print("Invalid data type entered.")
