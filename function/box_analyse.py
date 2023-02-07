from PIL import Image
from res import Result
from res import BoxView
from math import sqrt
from res import ImageInf


def analyse():
    pass


def fill_box_view(dict_a: dict, dict_b: dict, dict_c: dict, cur_dict: dict, res: Result):
    for _key in dict_c.keys():
        li = dict_c[_key]  # li: [["58", "0.389578", "0.416103", "0.038594", "0.163146"], [...]]
        l_a = dict_a[
            _key]  # [{'image_id': 298251, 'category_id': 24, 'bbox': [518.5, 102.75, 46.0, 42.25], 'score': 0.88916}]
        l_b = dict_b[_key]
        for _li in li:  # _li: ["58", "0.389578", "0.416103", "0.038594", "0.163146"]
            box_view = BoxView()
            box_view.category = _li[0]  # 58
            point = [_li[1], _li[2], _li[3], _li[4]]  # Had uniformized
            box_view.standard_box_point = point
            box_view.standard_box_area = (_li[3] * res.img_inf.width) * (_li[4] * res.img_inf.height)
            # A
            a_box_dict = dict()
            a_mini_dis = res.img_inf.diagonal  # The max length for img

            for d_a in l_a:  # d_a: {'image_id': 298251, 'category_id': 24, 'bbox': [0.389578, 0.626338, 0.389578, 0.389578], 'score': 0.88916}
                bbox = d_a['bbox']
                distance = sqrt(
                    pow(bbox[0] - point[0], 2) + pow(bbox[1] - point[1], 2))  # sqrt((ax - sx) ** 2 + (ay - sy) ** 2)
                if distance < a_mini_dis:
                    distance = a_mini_dis
                    a_box_dict = d_a

            bbox = a_box_dict['bbox']
            box_view.a_deviation_value_fiducial_point = a_mini_dis / res.img_inf.diagonal  # uniformize the distance by diagonal length in img
            box_view.a_box_area = (bbox[2] * res.img_inf.width) * (bbox[3] * res.img_inf.height)
            if box_view.a_box_area >= box_view.standard_box_area:
                box_view.a_is_bigger = True
            else:
                box_view.a_is_bigger = False
            box_view.a_standard_box_area_differ_rate = abs(box_view.a_box_area - box_view.standard_box_area) / box_view.standard_box_area
            box_view.a_score = a_box_dict['score']

            # B
            b_box_dict = dict()
            b_mini_dis = res.img_inf.diagonal

            for d_b in l_b:
                bbox = d_b['bbox']
                distance = sqrt(
                    pow(bbox[0] - point[0], 2) + pow(bbox[1] - point[1], 2))  # sqrt((bx - sx) ** 2 + (by - sy) ** 2)
                if distance < b_mini_dis:
                    distance = b_mini_dis
                    b_box_dict = d_b

            bbox = b_box_dict['bbox']
            box_view.b_deviation_value_fiducial_point = b_mini_dis / res.img_inf.diagonal  # uniformize the distance by diagonal length in img
            box_view.b_box_area = (bbox[2] * res.img_inf.width) * (bbox[3] * res.img_inf.height)
            if box_view.b_box_area >= box_view.standard_box_area:
                box_view.b_is_bigger = True
            else:
                box_view.b_is_bigger = False
            box_view.b_standard_box_area_differ_rate = abs(box_view.b_box_area - box_view.standard_box_area) / box_view.standard_box_area
            box_view.b_score = b_box_dict['score']


def box_size_uniformize(_dict: dict, img_dir_path: str, res: Result):
    keys = _dict.keys()
    for _key in keys:
        img_name = _key.zfill(12) + ".jpg"
        img_path = img_dir_path + "/" + img_name
        img = Image.open(img_path)
        img_size = img.size
        w = img.width
        h = img.height
        f = img.format
        li = _dict[
            _key]  # [{	'image_id': 298251, 'category_id': 24, 'bbox': [518.5, 102.75, 46.0, 42.25], 'score': 0.88916}]
        for _li in li:
            bbox = _li['bbox']
            bbox[0] = bbox[0] / w  # box_cx
            bbox[1] = bbox[1] / h  # box_cy
            bbox[2] = bbox[2] / w  # box_w
            bbox[3] = bbox[3] / h  # box_h

        img_inf = ImageInf(img_name, img_path, img_size, f, w, h, sqrt(pow(w, 2) + pow(h, 2)))  # diagonal sqrt
        res.img_inf = img_inf


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
