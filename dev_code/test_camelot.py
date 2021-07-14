"""
Camelot
"""
import camelot
import json

# Read the
password = ""
tables = camelot.read_pdf('test.pdf', password=password)
print("Found %d tables" % len(tables))

# Export to json
tables[0].to_json('test.json')

# Read json
with open('test.json') as f:
    data = json.load(f)
    print(data)
