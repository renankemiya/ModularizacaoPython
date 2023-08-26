import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def normalize(data):
    scaler = MinMaxScaler()
    scaler.fit(data)

    return pd.DataFrame(scaler.transform(data), columns=data.columns)
