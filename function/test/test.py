import json
import os
from collections import defaultdict

from function import val_func

# path = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/coco数据集/val2017/'
#
# with open('/Users/lumi/Documents/模型测试数据与对比需求分析 copy/coco数据集/val2017/000000000139.txt', 'r') as file:
#     for line in file:
#         str = line.split(' ')
#         print(str[1])
#         print(str[0])


# Standard val
dir3 = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/coco数据集/val2017/'
filename_list = val_func.get_fname(dir3)

dict_c = defaultdict(list)

for filename in filename_list:
    img_num = filename.split('.')[0]
    with open(dir3 + filename) as file:
        for line in file:  # Every line for val, for example: 22 0.161641 0.711069 0.101219 0.268553
            line = line.strip('\n')
            sres = line.split(' ')  # Split result
            category = sres[0]
            box_cx = sres[1]
            box_cy = sres[2]
            box_w = sres[3]
            box_h = sres[4]
            val_list = [category, box_cx, box_cy, box_w, box_h]
            dict_c[int(img_num)].append(val_list)  # val_dict:{298251:[category, box_cx, box_cy, box_w, box_h]}

print(dict_c)

