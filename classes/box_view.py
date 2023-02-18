import json


class BoxView:
    category: int
    standard_box_point: list
    standard_box_area: float
    a_box_point: list
    b_box_point: list
    a_deviation_value_fiducial_point: float
    b_deviation_value_fiducial_point: float
    a_box_area: float
    b_box_area: float
    a_is_bigger: bool  # a's area is bigger than standard
    b_is_bigger: bool  # b's area is bigger than standard
    a_standard_box_area_differ_rate: float
    b_standard_box_area_differ_rate: float
    a_score: float
    b_score: float

    def __init__(self):
        self.category = -1
        self.standard_box_point = []
        self.standard_box_area = 0
        self.a_box_point = []
        self.b_box_point = []
        self.a_deviation_value_fiducial_point = -1
        self.b_deviation_value_fiducial_point = -1
        self.a_box_area = 0
        self.b_box_area = 0
        self.a_is_bigger = True
        self.b_is_bigger = True
        self.a_standard_box_area_differ_rate = -1
        self.b_standard_box_area_differ_rate = -1
        self.a_score = 0
        self.b_score = 0

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
