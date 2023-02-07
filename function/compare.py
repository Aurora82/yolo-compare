from collections import defaultdict

import pred_func
import val_func


def Compare(dir1, dir2, dir3):
    """
    Make all function to run.
    :param dir1: A _prediction file directory.
    :param dir2: B _prediction file directory.
    :param dir3: Standard val folder directory.
    :return:
    """
    # YOLO improvement
    dict_a = pred_func.read(dir1)
    # YOLO
    dict_b = pred_func.read(dir2)





