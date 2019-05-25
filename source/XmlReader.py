import xml.etree.ElementTree as ET
import sys
import os
from source.DataObject import DataObject
from lxml import etree


class XmlReader:
    '''Class responsible for reading and preliminary validation of xml content'''

    def __init__(self, path):
        self.filePath = None
        self.Objects = []
        if os.path.isfile(path):
            self.filePath = path
        else:
            print('Could not open ', path, '. It\'s not a file or directory')
            sys.exit(-1)

        self.prepareFile()

        parser = etree.XMLParser(recover=True)
        self.tree = etree.parse(self.filePath, parser)
        self.root = self.tree.getroot()

    def prepareFile(self):
        '''Method preparing file if there is no root. '''

        with open(self.filePath, 'r+') as fp:
            lines = fp.readlines()
            if '<root>\n' not in lines[0]:
                lines.insert(0, '<root>\n')
                lines.append('</root>\n')

        with open(self.filePath, 'w+') as fp:
            fp.seek(0)
            fp.writelines(lines)

    def read(self):
        '''Xml reading and pre-validating method. Checks whether the data is printable.
            Returns list of DataObjects'''

        objectList = []
        for obj in self.root:
            data = None
            dataObject = None
            if obj.tag == 'object':
                for el in obj:
                    if str(el.text).isprintable():
                        if el.tag == 'obj_name':
                            if str(el.text) != 'None' and str(el.text) != '':
                                data = {'objName': str(el.text),
                                        'fields': []}
                                objectList.append(DataObject(str(el.text)))
                            else:
                                break

                    if el.tag == 'field':
                        toAppend = {'name': None,
                                    'type': None,
                                    'value': None}
                        for fat in el:
                            if str(fat.text).isprintable():
                                if fat.tag == 'name':
                                    toAppend['name'] = str(fat.text)
                                elif fat.tag == 'type':
                                    if fat.text == 'string' or fat.text == 'int':
                                        toAppend['type'] = str(fat.text)
                                elif fat.tag == 'value':
                                    toAppend['value'] = str(fat.text)
                        objectList[-1].setFields(**toAppend)
        return objectList


if __name__ == '__main__':
    pass
