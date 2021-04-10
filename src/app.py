import json
import numpy as np
import pandas as pd

def hello_pandas():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello Pandas!",
            "test"   : "pd.Series([1, 3, 5]).tolist()",
            "result" :  pd.Series([1, 3, 5]).tolist()
        }),
    }

def hello_numpy():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello Numpy!",
            "test"   : "np.array([1,2,3]).tolist()",
            "result" :  np.array([1,2,3]).tolist()
        }),
    }

def lambda_handler(event, context):
    return hello_pandas()
