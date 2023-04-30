import json


class Reader:
    #@staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as f:
            if file_path.endswith('.json'):
                return json.load(f)
            else:
                raise ValueError('This file should be .json')
