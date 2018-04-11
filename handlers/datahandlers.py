import numpy as np
import pandas as pd
import mimetypes

class PandasHandler:
    """ Abre arquivos ('csv','xls') para analise de dados """

    def get_dataset(self, dataset):
        """ Informa qual o dataset a ser trabalhado """
        return self.__pandas_read(dataset)

    def __get_mimetype_dataset(self, dataset):
        mimetype = mimetypes.guess_type(dataset)[0]
        return mimetypes.guess_extension(mimetype)

    def __pandas_read(self, dataset):
        dataframe = None
        mimetype = self.__get_mimetype_dataset(dataset)
        if mimetype == '.csv':
            dataframe = pd.read_csv(dataset)
        elif mimetype == 'xls':
            dataframe = pd.read_excel(dataset)
        # elif mimetype == 'sqlite':
        #     dataframe = pd.read_sql()
        else:
            self.__invalid_type()

        return dataframe

    def __invalid_type(self):
        raise TypeError('O arquivo indicado não é de um dos tipos válidos.')