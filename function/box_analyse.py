from res import Result
from res import BoxView
from math import sqrt
from img_func import img_inf_fill


def analyse(res: Result, dict_a: dict, dict_b: dict, dict_c: dict, image_id: int, deviation: int):
    print(res.image_id, " Uniformize Successful!")
    fill_box_view(res, dict_a, dict_b, dict_c, image_id, deviation)


def uniformize(res: Result, dict_a: dict, dict_b: dict):
    box_size_uniformize(dict_a, res)
    box_size_uniformize(dict_b, res)


def box_size_uniformize(_dict: dict, res: Result):
    """
    Uniformize the box position, width, height into between zero and one.
    :param _dict: dict_a, dict_b.
    :param res: Result class.
    :return: None
    """
    keys = _dict.keys()
    for _key in keys:
        for _li in _dict[_key]:
            # [{'image_id': 298251, ..., 'bbox': [518.5, 102.75, 46.0, 42.25], ...}]
            _li['bbox'] = get_uniformize(res, _li['bbox'])


def get_uniformize(res: Result, bbox: list):
    box = [0, 0, 0, 0]
    box[0] = float(bbox[0]) * int(res.img_inf.width)  # box_cx
    box[1] = float(bbox[1]) * int(res.img_inf.height)  # box_cy
    box[2] = float(bbox[2]) * int(res.img_inf.width)  # box_w
    box[3] = float(bbox[3]) * int(res.img_inf.height)  # box_h

    return box


def get_uniformize_restore(res: Result, bbox: list):
    box = [0, 0, 0, 0]
    box[0] = float(bbox[0]) * int(res.img_inf.width)  # box_cx
    box[1] = float(bbox[1]) * int(res.img_inf.height)  # box_cy
    box[2] = float(bbox[2]) * int(res.img_inf.width)  # box_w
    box[3] = float(bbox[3]) * int(res.img_inf.height)  # box_h
    return box


def fill_box_view(res: Result, dict_a: dict, dict_b: dict, dict_c: dict, image_id: int, deviation: int):
    li = dict_c[image_id]  # li: [["58", "0.389578", "0.416103", "0.038594", "0.163146"], [...]]
    l_a = dict_a[image_id]
    # [{'image_id': 298251, 'category_id': 24, 'bbox': [518.5, 102.75, 46.0, 42.25], 'score': 0.88916}]
    l_b = dict_b[image_id]

    for _li in li:  # _li: ["58", "0.389578", "0.416103", "0.038594", "0.163146"]
        box_view = BoxView()
        box_view.category = _li[0]  # 58
        point = [_li[1], _li[2], _li[3], _li[4]]  # Had uniformized
        box_view.standard_box_point = get_uniformize_restore(res, point)  # Not uniformed [518.5, 102.75, 46.0, 42.25]
        box_view.standard_box_area = (float(_li[3]) * res.img_inf.width) * (
                float(_li[4]) * res.img_inf.height)  # (0.038594 * 152) * (0.163146 * 124)

        # A
        a_box_dict = dict()
        a_mini_dis = res.img_inf.diagonal  # The max length for img
        for d_a in l_a:  # d_a: {'image_id': 298251, 'category_id': 24, 'bbox': [0.389578, 0.626338, 0.389578, 0.389578], 'score': 0.88916}
            bbox = d_a['bbox']
            distance = sqrt(
                pow(float(bbox[0]) - float(point[0]), 2) + pow(float(bbox[1]) - float(point[1]),
                                                               2))  # sqrt((ax - sx) ** 2 + (ay - sy) ** 2)
            if distance < a_mini_dis:
                a_mini_dis = distance
                a_box_dict = d_a

        if deviation < a_mini_dis:
            res.a_deviation_count = res.a_deviation_count + 1
        else:
            bbox = a_box_dict['bbox']
            box_view.a_deviation_value_fiducial_point = a_mini_dis / res.img_inf.diagonal  # uniformize the distance by diagonal length in img
            box_view.a_box_area = (bbox[2] * res.img_inf.width) * (bbox[3] * res.img_inf.height)

            if box_view.a_box_area >= box_view.standard_box_area:
                box_view.a_is_bigger = True
            else:
                box_view.a_is_bigger = False
            box_view.a_standard_box_area_differ_rate = abs(
                box_view.a_box_area - box_view.standard_box_area) / box_view.standard_box_area
            box_view.a_score = a_box_dict['score']

        # B
        b_box_dict = dict()
        b_mini_dis = res.img_inf.diagonal

        for d_b in l_b:
            bbox = d_b['bbox']
            distance = sqrt(
                pow(float(bbox[0]) - float(point[0]), 2) + pow(float(bbox[1]) - float(point[1]),
                                                               2))  # sqrt((bx - sx) ** 2 + (by - sy) ** 2)
            if distance < b_mini_dis:
                b_mini_dis = distance
                b_box_dict = d_b

        if deviation < b_mini_dis:
            res.b_deviation_count = res.b_deviation_count + 1
        else:
            bbox = b_box_dict['bbox']
            box_view.b_deviation_value_fiducial_point = b_mini_dis / res.img_inf.diagonal  # uniformize the distance by diagonal length in img
            box_view.b_box_area = (bbox[2] * res.img_inf.width) * (bbox[3] * res.img_inf.height)
            if box_view.b_box_area >= box_view.standard_box_area:
                box_view.b_is_bigger = True
            else:
                box_view.b_is_bigger = False
            box_view.b_standard_box_area_differ_rate = abs(
                box_view.b_box_area - box_view.standard_box_area) / box_view.standard_box_area
            box_view.b_score = b_box_dict['score']

        res.box_view.append(box_view)


def get_box_amount(_dict: dict, _key: int, res: Result):
    """
    Return the box amount mark in image.
    :param res:
    :param _key: image id. (Like: 139)
    :param _dict: YOLO dictionary, YOLO improvement dictionary or val's.
    :return:
    """

    box_amount = 0
    if not _dict.__contains__(_key):
        print("YOLO Improvement's Img " + str(_key) + " not found.")
    else:
        # list_a: [{'image_id': 298251, 'category_id': 24, 'bbox': [518.5, 102.75, 46.0, 42.25], 'score': 0.88916}]}
        # _key:139  l_c(list_c): [["58", "0.389578", "0.416103", "0.038594", "0.163146"]]
        li = _dict[_key]
        box_amount = len(li)

    # return box_amount
