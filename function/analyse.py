import pickle

from function import pred_func
from function import val_func
from function import category_analyse
from function import box_analyse
from function import img_func
from classes.res import Result

def compare(dict_a, dict_b, dict_c, img_dir, _key, deviation):
    print("_key: ", _key)  # "139": [["58", "0.389578", "0.416103", "0.038594", "0.163146"],...]
    res = Result()  # Result
    res.image_id = _key  # 139
    res.img_path = img_dir  #
    img_func.img_inf_fill(res, res.img_path, res.image_id)
    box_analyse.uniformize(res, dict_a, dict_b)
    category_analyse.analyse(res, dict_a, dict_b, dict_c, res.image_id)
    box_analyse.analyse(res, dict_a, dict_b, dict_c, res.image_id, deviation)
    return res


def read_from_file(dir1, dir2, dir3):
    dict_a = pred_func.json_read(dir1)  # YOLO improvement
    dict_b = pred_func.json_read(dir2)  # YOLO
    dict_c = val_func.trans_to_dict(dir3)  # Standard val
    return dict_a, dict_b, dict_c
