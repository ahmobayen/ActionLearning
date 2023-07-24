from datetime import datetime

import pandas as pd
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, Float, TIMESTAMP

from config import PSQL, TIME_STYLE


class DataModel:
    def __init__(self):
        self.engine = db.create_engine(PSQL, echo=False)
        self.engine = self.engine.execution_options(connect_args={'sslmode': 'require'})

        self.metadata = db.MetaData()
        if not db.inspect(self.engine).has_table('auto'):
            self.create_table()
        else:
            self.auto = db.Table('auto', self.metadata, autoload_with=self.engine)

    def write(self, data: pd.DataFrame):
        data.to_sql(name='auto', con=self.engine, if_exists='append', index=False)

    def write_training_file(self, data: pd.DataFrame):
        data.to_sql(name='training', con=self.engine, if_exists='fail')

    def write_log(self, data: pd.DataFrame, meta_id: str):
        data['meta_id'] = meta_id
        data.to_sql(name='gx_log', con=self.engine, if_exists='append', index=False)
        data.to_json(f"../logs/results_{meta_id}.json")

    def write_summery(self, data: pd.DataFrame, meta_id: str):
        data.to_sql(name='gx_summery', con=self.engine, if_exists='append', index=False)
        data.to_json(f"../logs/summery_{meta_id}.json")

    def read_all(self):
        query = self.auto.select()
        with self.engine.connect() as conn:
            result_proxy = conn.execute(query)
            result_set = result_proxy.fetchall()
        return pd.DataFrame(result_set).to_dict(orient='records')

    def filter_date(self, start_date, end_date):
        start_date = datetime.strptime(start_date, TIME_STYLE)
        end_date = datetime.strptime(end_date, TIME_STYLE)
        query = self.auto.select().filter(self.auto.c.created_at.between(start_date, end_date))
        with self.engine.connect() as conn:
            result_proxy = conn.execute(query)
            result_set = result_proxy.fetchall()
            return pd.DataFrame(result_set).to_dict(orient='records')

    def create_table(self):
        auto = Table(
            'auto', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('symboling', Integer),
        )
        self.metadata.create_all(bind=self.engine, checkfirst=True)


if __name__ == '__main__':
    data = pd.read_csv('../model/auto.csv')
    db = DataModel()
    # db.create_table()
    result = db.read_all()
    print(result)
    # db.write_training_file(data)
    # start_datetime = '2023-05-01 00:00:00.0'
    # end_datetime = '2023-05-14 00:00:00.0'
    #
    # db.filter_date(start_datetime,end_datetime)