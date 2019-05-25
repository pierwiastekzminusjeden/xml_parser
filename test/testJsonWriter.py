import unittest
from source.DataObject import DataObject
from source.JsonWriter import JsonWriter


class TestJsonWriter(unittest.TestCase):

    jw = JsonWriter('test/target/out.json')

    def test_checkObjectEmptyFields(self):
        # jw = JsonWriter('test/target/out.json')
        do = DataObject('test')
        self.assertEquals(False, self.jw.checkObject(do),)

    def test_checkObjectDifferentType(self):
        self.assertEquals(False, self.jw.checkObject({}),)

    def test_checkObjectCorrectFields(self):
        do = DataObject('test')
        testFields = {'name': 'test',
                      'type': 'string',
                      'value': 'test'}

        do.setFields(**testFields)
        self.assertEqual(True, self.jw.checkObject(do), 'String test')
        testFields = {'name': 'test',
                      'type': 'int',
                      'value': 12}

        do.setFields(**testFields)
        self.assertEqual(True, self.jw.checkObject(do), 'int test')

if __name__ == '__main__':
    unittest.main()
