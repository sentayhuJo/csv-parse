
import json
import pandas as pd

df = pd.read_csv('Young People and Children.csv')

records = []
for key, grp in df.groupby('Organisation'):

    records.append({
        "Organisation": grp.Organisation.iloc[0],
        "Area": grp.Area.iloc[0],
        "Borough": grp.Borough.iloc[0],
        "Services":grp.Services.iloc[0],
        "Website": grp.Website.iloc[0],
        "Day":[
            row.Day for row in grp.itertuples()
        ],
        "Clients": [
            row.Clients for row in grp.itertuples()
        ],
        "Tel": [
            row.Tel for row in grp.itertuples()
        ],
        "Email": grp.Email.iloc[0],
        "Postcode": grp.Postcode.iloc[0],
        "Process": [
            row.Process for row in grp.itertuples()
        ],
        'Catagory': 'Young People and Children'})
records = dict(data = records)
with open("Young People and Children.json", "w") as outfile:
    outfile.write(json.dumps(records, outfile ,indent=4))


