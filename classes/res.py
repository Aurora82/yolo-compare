import json
from classes.image_inf import ImageInf


class Result:
    image_id: int
    img_path: str
    img_inf: ImageInf

    category_view: list
    standard_category_amount: int
    a_category_amount: int
    b_category_amount: int
    a_category_miss_amount: int  # The amount of not match with standard category
    b_category_miss_amount: int  # The amount of not match with standard category

    a_category_coverage_rate: float
    b_category_coverage_rate: float

    box_view: list

    standard_box_amount: int

    a_box_amount: int
    a_box_coverage_rate: float
    a_comprehensive_evaluation: float

    b_box_amount: int
    b_box_coverage_rate: float
    b_comprehensive_evaluation: float

    a_deviation_count: int
    b_deviation_count: int

    def __init__(self):
        self.image_id = 0
        self.img_path = ''
        self.img_inf = ImageInf("untitled", "/", "none", None, 0, 0, 0)
        self.category_view = list()
        self.standard_category_amount = 0
        self.a_category_amount = 0
        self.b_category_amount = 0
        self.a_category_miss_amount = 0
        self.b_category_miss_amount = 0
        self.a_category_coverage_rate = 0
        self.b_category_coverage_rate = 0
        self.box_view = list()
        self.standard_box_amount = 0
        self.a_box_amount = 0
        self.a_box_coverage_rate = 0
        self.a_comprehensive_evaluation = 0
        self.b_box_amount = 0
        self.b_box_coverage_rate = 0
        self.b_comprehensive_evaluation = 0
        self.a_deviation_count = 0
        self.b_deviation_count = 0

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
