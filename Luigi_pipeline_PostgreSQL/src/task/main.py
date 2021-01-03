import luigi
from luigi.contrib import sqla
import pandas as pd
from task import spreadsheet, connection_string


class InsertDictionaryTask(sqla.CopyToTable):
    
    reflect = True
    connection_string = connection_string
    table = "dictionary"
    dictionary_data = pd.read_excel(spreadsheet, 'dictionary')

    def rows(self):
        for index, row in self.dictionary_data.iterrows():
            yield row


class InsertPricesTask(sqla.CopyToTable):

    reflect = True
    connection_string = connection_string
    table = "prices"
    prices_data = pd.read_excel(spreadsheet, 'prices')

    def rows(self):
        for index, row in self.prices_data.iterrows():
            yield row


class RunAllTasks(luigi.Task):

    def requires(self):
        yield InsertDictionaryTask()
        yield InsertPricesTask()


if __name__ == '__main__':

    env_params = {'local_scheduler': True, }
    task = RunAllTasks()
    luigi.build([task], **env_params)