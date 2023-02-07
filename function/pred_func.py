import json
from collections import defaultdict


# dir1 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/YOLOv5改进结果/_predictions.json'
# dir2 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/YOLOv5/_predictions.json'
# dir3 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/coco数据集/val2017'

def json_read(file_dir):
    json_dict = defaultdict(list)
    with open(file_dir, 'r') as _prediction:
        _prediction_A_data = json.load(_prediction)

        for item in _prediction_A_data:
            json_dict[item['image_id']].append(item)

        return json_dict
