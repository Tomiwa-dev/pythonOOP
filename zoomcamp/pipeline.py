import pandas as pd 
from sqlalchemy import create_engine 
import os
import argparse
import pyarrow.parquet as pq

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
    filename = 'output.parquet'
    
    os.system(f"wget {url} -O {filename}")


    parquet_table = pq.read_table(filename)
    df = parquet_table.to_pandas()

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    #df.to_sql(name='yellow_taxi_data',con=engine, if_exists='append', chunksize=100000)


    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Ingest data to Postgres')

        parser.add_argument('--user', required=True, help='user name for postgres')
        parser.add_argument('--password', required=True, help='password for postgres')
        parser.add_argument('--host', required=True, help='host for postgres')
        parser.add_argument('--port', required=True, help='port for postgres')
        parser.add_argument('--db', required=True, help='database name for postgres')
        parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
        parser.add_argument('--url', required=True, help='url of the parquet file')

        args = parser.parse_args()

        main(args)


