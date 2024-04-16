import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def read_data(file_name: str, file_type: str):
    if file_type.lower() == "csv":
        return pd.read_csv(file_name)
    elif file_type.lower() == "excel":
        return pd.read_excel(file_name)
    elif file_type.lower() == "json":
        return pd.read_json(file_name)
    else:
        raise ValueError("try one from these types: csv, excel, and json")


def summary(data_frame: pd.DataFrame):
    pd.set_option('display.width', 5000)
    print("summary of numeric attribute:\n",data_frame.describe(),"\n")
    print("summary of object attribute:\n",data_frame.describe(include=object),"\n")
    
    


def handle_missing_values(data_frame: pd.DataFrame, way: str, value=None,stratgy=None):
    if way == "fill":
        if value == None and stratgy==None:
            raise ValueError("Enter the value or the strategy")
        elif stratgy=="mean":
            data_frame.fillna(np.mean(data_frame), inplace=True)
        elif stratgy=="median":
            data_frame.fillna(np.median(data_frame), inplace=True)
        elif stratgy=="mode":
            data_frame.fillna(np.argmax(np.bincount(data_frame)), inplace=True)
        else:
            data_frame.fillna(value, inplace=True)
    elif way == "drop":
        data_frame.dropna(inplace=True)
    else:
        raise ValueError("enter a correct way.")


def encoding(data:pd.DataFrame,column: pd.Series,is_ordinal:bool):
    if is_ordinal==True or data[column].nunique==2:
        le=LabelEncoder()
        data[column]=le.fit_transform(data[column])
    else:
        
       return  pd.get_dummies(data,columns=column,drop_first=True)
        
        
def Encoding(column: pd.Series,is_ordinal:bool):
   keys = column.unique()
   return column.apply(lambda x: np.where(keys == x)[0][0])