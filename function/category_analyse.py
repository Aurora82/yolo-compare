from res import Result
from res import CategoryView


def analyse(dict_a: dict, dict_b: dict, dict_c: dict, image_id: int, res: Result):
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

    fill_category_view(a_pred_dict, b_pred_dict, c_pred_dict, a_pred_dict, res)
    fill_category_view(a_pred_dict, b_pred_dict, c_pred_dict, b_pred_dict, res)
    fill_category_view(a_pred_dict, b_pred_dict, c_pred_dict, c_pred_dict, res)


def category_coverage_rate_analyse(res: Result):
    """
    Get the coverage rate between the category amount in YOLO analysis and standard category amount.
    :param res: Class res.Result
    :return:
    """
    a_coverage_box_amount = 0
    b_coverage_box_amount = 0
    standard_coverage_box_amount = 0
    li = res.category_view
    for _li in li:
        standard_coverage_box_amount += _li.standard_box_category_amount
        if not _li.standard_category == -1:
            if not _li.a_category == -1:
                a_coverage_box_amount += 1
            if not _li.b_category == -1:
                b_coverage_box_amount += 1
    res.a_category_coverage_rate = float(a_coverage_box_amount) / standard_coverage_box_amount
    res.b_category_coverage_rate = float(b_coverage_box_amount) / standard_coverage_box_amount


def fill_category_view(a_pred_dict: dict, b_pred_dict: dict, c_pred_dict: dict, cur_dict: dict, res: Result):
    for _key in cur_dict.keys():
        view = CategoryView()
        # C category view
        if c_pred_dict.__contains__(_key):
            view.standard_category = _key  # '139'
            view.standard_category_box_amount = c_pred_dict[_key]
            c_pred_dict.pop(_key)
        else:
            view.standard_category = -1
            view.standard_category_box_amount = -1
        # A category view
        if a_pred_dict.__contains__(_key):
            view.a_category = _key
            view.a_category_box_amount = a_pred_dict[_key]
            a_pred_dict.pop(_key)  # Pop all keys the same with dict_c
        else:
            view.a_category = -1
            view.a_category_box_amount = -1
        # B category view
        if b_pred_dict.__contains__(_key):
            view.b_category = _key
            view.b_category_box_amount = b_pred_dict[_key]
            b_pred_dict.pop(_key)  # Pop all keys the same with dict_c
        else:
            view.b_category = -1
            view.b_category_box_amount = -1

        res.category_view.append(view)


def get_category_amount(_dict: dict, image_id: int):
    _li = _dict[image_id]  # li: [{'image_id': 298251, 'category_id': 24, ...
    return len(_li)


def pred_category_detail_analyse(_dict: dict, _key: int):
    """
    Standard val category analyse.
    :param _dict: A or B dictionary.
    :param _key: image id. (Like: 139)
    :return:
    """
    pred_dict = dict()  # {category_id: num}
    li = _dict[_key]
    for _li in li:  # li: [{'image_id': 298251, 'category_id': 24, 'bbox': [518.5, 102.75, 46.0, 42.25], 'score': 0.88916}]
        par = _li['image_id']  # "298251"
        # count the number of every category_id in dict_pred(A or B)
        if pred_dict.__contains__(par):
            pred_dict[par] += 1
        else:
            pred_dict.setdefault(par, 1)
    return pred_dict


def val_category_detail_analyse(_dict: dict, _key: int):
    """
    Standard val category analyse.
    :param _dict:
    :param _key: image id. (Like: 139)
    :return:
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
