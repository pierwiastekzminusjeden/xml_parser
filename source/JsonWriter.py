from source.DataObject import DataObject
import json

class JsonWriter:
    '''Class responsible for creating json files'''

#todo outName validation
#class refactor, multiple types of outfile
    def __init__(self, outName):
        self.outputFile = outName
        f = open(self.outputFile, 'w+')
        f.close()

    def writeFromString(self, dataObjectList):
        '''Method for preparing the output json file'''

        isFirst = True
        toPrint = '{'
        for o in dataObjectList:
            if isFirst:
                isFirst = False
            else:
                toPrint +=','
                if not self.checkObject(o):
                    continue

            toPrint += str(o)
        toPrint += '}'

        parsed = json.loads(toPrint)
        with open(self.outputFile, 'a+') as f:
            json.dump(parsed, f, indent=4)

    def checkObject(self, dataObject):
        '''Method to check if the object should be added to json'''

        if not dataObject:
            return False
        if dataObject.fields:
            return True
        return False


if __name__ == '__main__':
    pass
