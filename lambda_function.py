import json
import pandas as pd

def lambda_handler(event, context):
    df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
    #df = pd.read_parquet(id + "/" + file1)                   
    #other = pd.read_parquet(id + "/" + file2)
    other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'B': ['B0', 'B1', 'B2'],
                      'C': ['B0', 'B1', 'B2'],
                      'D': ['B0', 'B1', 'B2']},
                      )
    df2 = df.join(other.set_index('key'), on='key')
    print(df2[["key","A"]].to_string())
    #df2.to_json("./out.json")
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
