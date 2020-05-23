from code_folder.read_data import read_json_data
from setting import logger


class MyObject:
    """This class create a Python object with a his associated methods

        Attributes:
            data: A boolean indicating if we like SPAM or not.
            list_item: An integer count of the eggs we have laid.
        """

    CONVERSION_DICT = {"un": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5}

    def __init__(self, data_path):
        self.data = read_json_data(data_path)
        self.list_item = self.extract_item_from_data()

    def extract_item_from_data(self):
        """
        This function extract items from json data
        Returns:
            list of item
        """
        return [elem["item"] for elem in self.data["elements"]]

    def convert_item_type(self, conversion_dict: dict):
        """
        This function convert string item in int item
        Args:
            conversion_dict (dict): dictionary for convert type of item
        Returns:
            list of item
        """
        list_item_converted = []
        for index, item in enumerate(self.list_item):
            try:
                list_item_converted.append(int(item))
            except ValueError:
                logger.info(" '%s' at index %s is not an integer", item, index)
                list_item_converted.append(conversion_dict[item])
        return list_item_converted
