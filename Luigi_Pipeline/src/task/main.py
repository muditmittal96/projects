import luigi
from luigi.contrib import sqla
from task import spreadsheet, connection_string
import pandas as pd


class InsertDictionaryTask(sqla.CopyToTable):
    
    connection_string = connection_string
    reflect = True
    table = "dictionary"
    data = pd.read_excel(spreadsheet, 'dictionary')

    def rows(self):
        for index, row in self.data.iterrows():
            yield row


class InsertPricesTask(sqla.CopyToTable):

    connection_string = connection_string
    reflect = True
    table = "prices"
    data = pd.read_excel(spreadsheet, 'prices')

    def rows(self):
        for index, row in self.data.iterrows():
            yield row


class RunAllTasks(luigi.Task):

    def requires(self):
        yield InsertDictionaryTask()
        yield InsertPricesTask()


if __name__ == '__main__':

    env_params = {'local_scheduler': True, }
    task = RunAllTasks()
    luigi.build([task], **env_params)