from classes.res import Result
from classes.category_view import CategoryView


def analyse(res: Result, dict_a: dict, dict_b: dict, dict_c: dict, image_id: int):
    """
    Justify the category number of _prediction and val right or not.
    :param res:
    :param dict_a: dict a (YOLO improvement's _prediction).
    :param dict_b: dict b (YOLO's _prediction).
    :param dict_c: dict of val comparison.
    :param image_id:
    :param res:
    :return:
    """
    a_pred_dict = pred_category_detail_analyse(dict_a, image_id)
    b_pred_dict = pred_category_detail_analyse(dict_b, image_id)
    c_pred_dict = val_category_detail_analyse(dict_c, image_id)

    keys_a, keys_b, keys_c = a_pred_dict.keys(), b_pred_dict.keys(), c_pred_dict.keys()
    union_keys = set(keys_a).union(keys_b).union(keys_c)
    # print(union_keys)

    fill_category_view(a_pred_dict, b_pred_dict, c_pred_dict, union_keys, res)
    print('--------------------')
    res.a_category_coverage_rate = float(res.standard_category_amount - res.a_category_miss_amount) / res.standard_category_amount
    res.b_category_coverage_rate = float(res.standard_category_amount - res.b_category_miss_amount) / res.standard_category_amount

# def category_coverage_rate_analyse(res: Result):
#     """
#     Get the coverage rate between the category amount in YOLO analysis and standard category amount.
#     :param res: Class res.Result
#     :return:
#     """
#     a_coverage_box_amount = 0
#     b_coverage_box_amount = 0
#     standard_coverage_box_amount = 0
#     li = res.category_view
#     for _li in li:
#         standard_coverage_box_amount += _li.standard_box_category_amount
#         if not _li.standard_category == -1:
#             if not _li.a_category == -1:
#                 a_coverage_box_amount += 1
#             if not _li.b_category == -1:
#                 b_coverage_box_amount += 1
#     res.a_category_coverage_rate = float(a_coverage_box_amount) / standard_coverage_box_amount
#     res.b_category_coverage_rate = float(b_coverage_box_amount) / standard_coverage_box_amount

def category_amount(a_pred_dict: dict, b_pred_dict: dict, c_pred_dict: dict, res: Result):
    res.a_category_amount = len(a_pred_dict.keys())
    res.b_category_amount = len(b_pred_dict.keys())
    res.standard_category_amount = len(c_pred_dict.keys())


def fill_category_view(a_pred_dict: dict, b_pred_dict: dict, c_pred_dict: dict, union_keys: set, res: Result):
    """
    Fill all the property of category view classes.
    :param a_pred_dict: dict[category: num]
    :param b_pred_dict: dict[category: num]
    :param c_pred_dict: dict[category: num]
    :param union_keys: set{num, num, ...}
    :param res: Result
    :return: None
    """
    for _key in union_keys:  # _key is category id
        view = CategoryView()
        # C category view
        if c_pred_dict.__contains__(_key):
            view.standard_category = _key  # '139'
            view.standard_category_box_amount = c_pred_dict[_key]
            res.standard_category_amount += 1
            if not a_pred_dict.__contains__(_key):
                # If _key is contain in dict_c, but not in dict_a.
                # It means that dict_c's _key is missed in dict_a.
                res.a_category_miss_amount += 1
            if not b_pred_dict.__contains__(_key):
                # If _key is contain in dict_c, but not in dict_b.
                # It means that dict_c's _key is missed in dict_b.
                res.b_category_miss_amount += 1
        else:
            view.standard_category = -1
            view.standard_category_box_amount = -1
        # A category view
        if a_pred_dict.__contains__(_key):
            view.a_category = _key
            view.a_category_box_amount = a_pred_dict[_key]
        else:
            view.a_category = -1
            view.a_category_box_amount = -1

        # B category view
        if b_pred_dict.__contains__(_key):
            view.b_category = _key
            view.b_category_box_amount = b_pred_dict[_key]
        else:
            view.b_category = -1
            view.b_category_box_amount = -1

        res.category_view.append(view)

    # category_coverage_rate_reckon(res)


def category_coverage_rate_reckon(res: Result):
    pass


def pred_category_detail_analyse(_dict: dict, _key: int):
    """
    Analyse predict val how much box in every category.
    :param _dict: A or B dictionary.
    :param _key: image id. (Like: 139)
    :return: pred_dict[category: box number]
    """
    pred_dict = dict()  # {category_id: num}
    li = _dict[_key]
    for _li in li:  # li: [{'image_id': 298251, 'category_id': 24, 'bbox': [518.5, 102.75, 46.0, 42.25], 'score': 0.88916}]
        par = _li['category_id']  # "298251"
        # count the number of every category_id in dict_pred(A or B)
        if pred_dict.__contains__(par):
            pred_dict[par] += 1
        else:
            pred_dict.setdefault(par, 1)
    return pred_dict


def val_category_detail_analyse(_dict: dict, _key: int):
    """
    Analyse standard val how much box in every category.
    :param _dict: Standard dict.
    :param _key: image id. (Like: 139)
    :return: val_dict[category: box number]
    """
    val_dict = dict()  # {category_id: num}
    li = _dict[_key]
    for _li in li:  # list: ["58", "0.389578", "0.416103", "0.038594", "0.163146"]
        par = _li[0]  # "58"
        # count the number of every category_id in dict_c
        if val_dict.__contains__(par):
            val_dict[par] += 1
        else:
            val_dict.setdefault(par, 1)
    return val_dict
