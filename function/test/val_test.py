import json
import os
from collections import defaultdict

dir1 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/YOLOv5改进结果/_predictions.json'
dir2 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/YOLOv5/_predictions.json'
dir3 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/coco数据集/val2017/'

folder_dir = dir3
path = folder_dir
files = os.listdir(path)  # Use listdir read all files in path
files.sort()

fname_list = []
for file_ in files:
    if not os.path.isdir(path + file_):
        f_name = str(file_)
        fname_list.append(f_name)

# Standard val
filename_list = fname_list

dict_c = defaultdict(list)  # Set a default dict

for filename in filename_list:  # Eg. 000000000139.txt in [000000000139.txt, ...]
    img_num = filename.split('.')[0]  # 000000000139
    with open(dir3 + filename) as file:  # Open 000000000139.txt
        for line in file:  # Every line for val, for example: 22 0.161641 0.711069 0.101219 0.268553
            line = line.strip('\n')  # Get rid of \n for the end of line
            sres = line.split(' ')  # Split result
            category_id = sres[0]
            box_cx = sres[1]
            box_cy = sres[2]
            box_w = sres[3]
            box_h = sres[4]
            val_list = [category_id, box_cx, box_cy, box_w, box_h]
            dict_c[int(img_num)].append(val_list)  # val_dict:{298251:[category_id, box_cx, box_cy, box_w, box_h]}


with open('/Users/lumi/Git/YOLO_Analysis/function/test/_val_test_data', 'w') as _val_test_data:
    _val_test_data_json = json.dumps(dict_c)
    _val_test_data.write(_val_test_data_json)
    print("Complete!")