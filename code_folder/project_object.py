from code_folder.read_data import read_json_data


class MyObject:

    CONVERSION_DICT = {
        "un": 1,
        "deux": 2,
        "trois": 3,
        "quatre": 4,
        "cinq": 5
    }

    def __init__(self, data_path):
        self.data = read_json_data(data_path)
        self.list_item = self.extract_item_from_data()

    def extract_item_from_data(self):
        return [elem["item"] for elem in self.data["elements"]]

    def convert_item_type(self):
        list_item_converted = []
        for item in self.list_item:
            try:
                list_item_converted.append(int(item))
            except ValueError:
                list_item_converted.append(MyObject.CONVERSION_DICT[item])
        return list_item_converted
