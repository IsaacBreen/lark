"Transformer for evaluating csv.lark"

from lark import Transformer

class CsvTreeToPandasDict(Transformer):
    INT = int
    FLOAT = float
    SIGNED_FLOAT = float
    WORD = str
    NON_SEPARATOR_STRING = str

    def row(self, children):
        return children

    def start(self, children):
        header = children[0].children
        data = {heading: [] for heading in header}
        for row in children[1:]:
            for i, element in enumerate(row):
                data[header[i]].append(element)

        return data
