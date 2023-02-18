import json
from collections import defaultdict


def json_read(file_dir):
    json_dict = defaultdict(list)
    with open(file_dir, 'r') as _prediction:
        _prediction_A_data = json.load(_prediction)

        for item in _prediction_A_data:
            json_dict[item['image_id']].append(item)

        return json_dict
