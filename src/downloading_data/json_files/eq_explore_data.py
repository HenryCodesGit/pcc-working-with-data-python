from os import getcwd

from pathlib import Path
import json

# Read the data
filePath = Path(getcwd() + '/eq_data_1_day_m1.geojson')
contents = filePath.read_text()
contents_json = json.loads(contents)

# Create a more readable version of the data file
outputPath = Path(getcwd() + '/readable_eq_data.geojson')
readable_contents = json.dumps(contents_json, indent=4)
outputPath.write_text(readable_contents)