import pandas as pd
import json


##topics = ["Artificial-Intelligence-Foundations","Generative-AI","Machine-Learning","Natural-Language-Processing-nlp","Neural-Networks-and-Deep-Learning",
##          "Data-Analysis","Data-Visualization","Business-Intelligence","Tech-Career-Skills","Data-Engineering",
##          "Database-Development","Database-Administration","Data-Resource-Management","Data-Centers"]
##
topics = ["Data-Science"]
for topic in topics:
    csv_name = topic + "_json.csv"
# Read the CSV file into a DataFrame
    df = pd.read_csv(csv_name)
    
    # Initialize a list to hold parsed JSON objects
    full_data = []
    # Parse each row as JSON
    for index, row in df.iterrows():
        json_string = row.iloc[0]
        data = json.loads(json_string)

    ##    print(data['name'])
    ##    print(data['dateCreated'])
    ##    print(data['totalHistoricalEnrollment'])
    ##    print(data['description'])
        tags = []
        for i in range(len(data['about'])):
            tags.append(data['about'][i]['name'])
        parsed_json_data = [topic,data['name'],data['dateCreated'],data['totalHistoricalEnrollment'],data['description'],tags]
        full_data.append(parsed_json_data)

    df = pd.DataFrame(full_data)
    filename = topic + "_data.csv"
    df.to_csv(filename,sep =';',index=False)
