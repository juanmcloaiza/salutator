import pandas as pd
from .eso_table import EsoTable


class EsoColumn():
    def __init__(self, column_name, table_name, data):
        self._name = column_name
        self._table_name = table_name
        self._data = data

    def __getitem__(self, key):
        if self._data is None:
            self._data = [1, 2, 3]
        return self._data[key]


class ObsCore(EsoTable):
    """
    obscore table
    """

    def __init__(self, df: pd.DataFrame = pd.DataFrame()):
        self._df = df
        self._name = "ivoa.ObsCore"
        self._colnames = None
        for key in df.columns:
            self.__dict__[key] = EsoColumn(key, self._name, self._df[key])

    @property
    def colnames(self):
        if not self._colnames:
            self._colnames = list(self._df.columns)

        return self._colnames

    @colnames.setter
    def colnames(self, value):
        raise ValueError("Property cannot be modified by user")

    def __getitem__(self, key):
        return self._df[key]
