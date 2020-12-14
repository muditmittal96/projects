

import luigi
from luigi.contrib import sqla
import pandas as pd 
from task import spreadsheet, connection_string


class InsertDictionaryTask(sqla.CopyToTable):

    pass


class InsertPricesTask(sqla.CopyToTable):

    pass


class RunAllTasks(luigi.Task):

    def requires(self):
        yield InsertDictionaryTask()
        yield InsertPricesTask()



if __name__ == '__main__':
    
    env_params = {'local_scheduler': True,}
    task = RunAllTasks()
    luigi.build([task], **env_params)