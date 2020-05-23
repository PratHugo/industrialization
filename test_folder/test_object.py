import os
import unittest

from code_folder.project_object import MyObject


class TestMyObject(unittest.TestCase):

    DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data_test_folder/data.json"

    def test_data_type(self):
        result_data = MyObject(TestMyObject.DATA_PATH).data
        assert(type(result_data) == dict)

    def test_convert_item(self):
        result_list = \
            MyObject(TestMyObject.DATA_PATH).convert_item_type(MyObject.CONVERSION_DICT)
        assert(len(result_list) == 5)


if __name__ == '__main__':
    unittest.main()