import json
import pandas as pd
import os 
keys_to_use = ['id','all_artists','title','medium','acquisitionYear','height','width','units']

def get_record_from_file(file_path,keys_to_use):
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)
    record = []
    for field in keys_to_use:
        record.append(content[field])
    return tuple(record )
def read_artworks_from_json(keys_to_use):
    json_root = os.path.join('C:\\Users\\kiran\\Downloads\\collection-master\\artworks')
    artworks = []
    for root,_,files in os.walk(json_root):
        for f in files:
            if f.endswith('json'):
                record= get_record_from_file(os.path.join(root,f),keys_to_use)
                artworks.append(record)
            break
    df = pd.DataFrame.from_records(artworks,columns=keys_to_use,index='id')
    return df
df = read_artworks_from_json(keys_to_use)
print(df)