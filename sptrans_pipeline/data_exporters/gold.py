import os
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data(df: DataFrame, *args, **kwargs):
    path = '/home/src/sptrans_gold'
    os.makedirs(path, exist_ok=True)
    
    df.to_parquet(path, partition_cols=['data_extracao'], engine='pyarrow')