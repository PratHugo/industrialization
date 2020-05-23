import unittest

from code_folder.project_object import MyObject
from setting import project_local_path


class TestMyObject(unittest.TestCase):

    DATA_PATH = "data_folder/data.json"

    def test_data_type(self):
        result_data = MyObject(project_local_path.parent / TestMyObject.DATA_PATH).data
        assert(type(result_data) == dict)

    def test_convert_item(self):
        result_list = \
            MyObject(project_local_path.parent / TestMyObject.DATA_PATH).convert_item_type(MyObject.CONVERSION_DICT)
        assert(len(result_list) == 5)
