import json
from collections import defaultdict

from function import pred_func
from function import val_func
from function import category_analyse
from function import box_analyse
from function import img_func
from function.res import Result


def compare(dir1, dir2, dir3, img_dir):
    """
    Make all function to run.
    :param img_dir:
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
    res_dict = dict()
    # Image ids
    keys = dict_c.keys()

    img_dir_path = img_dir
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
        res_dict[res.image_id] = res

        count += 1
        if count > 2:
            break

    # with open("/Users/lumi/Git/YOLO_Analysis/function/test/res.txt", 'w') as res:
    #     res.write(json.dumps(res_list))
    for li in res_dict.keys():
        print(res_dict[li])
    return res_dict

