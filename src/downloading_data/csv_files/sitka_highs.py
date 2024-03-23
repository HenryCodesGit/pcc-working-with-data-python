from pathlib import Path
from datetime import datetime
import csv

# Current directory
currdir = Path(__file__).resolve().parent

#Import data
path = currdir / 'sitka_weather_2021_simple.csv'

lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperature
dates, highs, lows = [], [], []

# Iterate through the remainng rows in reader
# Pull only the high temp column
for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        highs.append(high)

print(highs)