import json
from collections import defaultdict
import img_func
import pred_func
import val_func
import category_analyse
import box_analyse
from res import Result


def Compare(dir1, dir2, dir3):
    """
    Make all function to run.
    :param dir1: A _prediction file directory.
    :param dir2: B _prediction file directory.
    :param dir3: Standard val folder directory.
    :return:
    """
    # YOLO improvement
    dict_a = pred_func.json_read(dir1)
    # YOLO
    dict_b = pred_func.json_read(dir2)
    # Standard val
    dict_c = val_func.trans_to_dict(dir3)
    # Result list
    res_list = list()
    # Image ids
    keys = dict_c.keys()

    img_dir_path = '/Users/lumi/Documents/模型测试数据与对比需求分析 copy/val2017'
    count = 0
    for _key in keys:  # "139": [["58", "0.389578", "0.416103", "0.038594", "0.163146"],...]
        print("_key: ", _key)
        res = Result()  # Result
        res.image_id = _key
        res.img_path = img_dir_path
        img_func.img_inf_fill(res, res.img_path, res.image_id)
        box_analyse.uniformize(res, dict_a, dict_b)

        # 1. analyse the category
        category_analyse.analyse(res, dict_a, dict_b, dict_c, res.image_id)
        res.a_category_coverage_rate = ''
        res.b_category_coverage_rate = ''
        box_analyse.analyse(res, dict_a, dict_b, dict_c, res.image_id, 100)
        res.a_box_amount = 0
        res.a_box_coverage_rate = 0
        res.b_box_amount = 0
        res.b_box_coverage_rate = 0
        res.a_comprehensive_evaluation = 0
        res.b_comprehensive_evaluation = 0
        res_list.append(res.__dict__)
        # count += 1
        # if count > 4:
        break

    # with open("/Users/lumi/Git/YOLO_Analysis/function/test/res.txt", 'w') as res:
    #     res.write(json.dumps(res_list))
    for li in res_list:
        print(li)

