import json
from collections import defaultdict

import pred_func
import val_func
import category_analyse
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

    dict_c = val_func.trans_to_dict(dir3)

    res_list = list()

    keys = dict_c.keys()

    for _key in keys:  # "139": [["58", "0.389578", "0.416103", "0.038594", "0.163146"],...]
        res = Result()
        res.image_id = _key
        res.img_path = ''

        # 1. analyse the category
