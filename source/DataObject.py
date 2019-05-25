

class DataObject(object):
    '''A class that represents the data object'''

    def __init__(self, name):
        self.objName = name
        self.fields = {}

    def setFields(self, **data):
        '''Method of class validating and inserting attributes of this object'''

        for key, value in data.items():
            if value is None:
                return
        try:
            if isinstance(int(data['value']), int) and data['type'] == 'int':
                self.fields.setdefault(data['name'], data['value'])
            elif isinstance(int(data['value']), int) and data['type'] == 'string':
                self.fields.setdefault(data['name'], data['value'])
        except ValueError:
            if isinstance(data['value'], str) and data['type'] == 'string':
                self.fields.setdefault(data['name'], data['value'])

    def __str__(self):
        ''' Method returns string with object content in json format'''

        string = '"' + self.objName + '": {\n'
        isFirst = True
        for key, value in self.fields.items():
            if isFirst:
                isFirst = False
            else:
                string += ',\n'

            string += '"' + key + '": '
            try:
                if isinstance(int(value), int):
                    string += value + ''
            except ValueError:
                if isinstance(value, str):
                    string += '"' + value + '"'
            # else:
            #     string += value + ',\n'
        string += '\n}'
        return string


if __name__ == '__main__':
    pass
