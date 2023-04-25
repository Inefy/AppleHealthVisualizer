# Apple Health Data Analyzer

This Python application allows you to analyze and visualize your Apple Health data, including sleep, heart rate, and steps. The script processes the data exported from the Apple Health app and creates clear, easy-to-read visualizations, which include various statistics like mean, median, and mode.

## Features

- Analyze and visualize sleep data, including light sleep, deep sleep, and REM sleep
- Analyze and visualize heart rate data
- Analyze and visualize step count data
- Filter data by date range

## Getting Started

### Prerequisites

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Numpy
- xml.etree.ElementTree

To install the required packages, run the following command:

```bash
pip install pandas matplotlib seaborn numpy
```

### Usage

1. Export your Apple Health data from the Health app on your iPhone. Instructions can be found [here](https://support.apple.com/en-us/HT203037).
2. Place the `export.xml` file in the same directory as the scripts or provide the file path to the script.
3. Run the `main.py` script:

```bash
python main.py
```

4. Follow the prompts to enter the data type you want to analyze (sleep, heart_rate, or steps), as well as the start and end dates for the data range.
5. The script will process the data and generate a visualization with statistics.

## Contributing

Contributions are welcome! Feel free to submit a pull request or report any issues you encounter while using the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.