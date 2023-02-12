import json


class CategoryView:
    # -1 stand for not found.
    standard_category: int
    standard_category_box_amount: int
    a_category: int
    a_category_box_amount: int
    b_category: int
    b_category_box_amount: int

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

class BoxView:
    category: int
    standard_box_point: list
    standard_box_area: float
    a_box_point: list
    a_deviation_value_fiducial_point: float
    a_box_area: float
    a_is_bigger: bool  # a's area is bigger than standard
    a_standard_box_area_differ_rate: float
    a_score: float

    b_box_point: list
    b_deviation_value_fiducial_point: float
    b_box_area: float
    b_is_bigger: bool  # b's area is bigger than standard
    b_standard_box_area_differ_rate: float
    b_score: float

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

class ImageInf:
    name: str
    path: str
    format: str
    size: tuple
    width: int
    height: int
    diagonal: float
    is_full: bool

    def __init__(self, name, path, _format, size, width, height, diagonal):
        self.name = name
        self.path = path
        self._format = _format
        self.size = size
        self.width = width
        self.height = height
        self.diagonal = diagonal
        self.is_full = False

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


class Result:
    image_id: int
    img_path: str
    img_inf: ImageInf

    category_view: list
    a_category_coverage_rate: float
    b_category_coverage_rate: float

    box_view: list
    a_box_amount: int
    a_box_coverage_rate: float
    a_comprehensive_evaluation: float

    b_box_amount: int
    b_box_coverage_rate: float
    b_comprehensive_evaluation: float

    a_deviation_count: int
    b_deviation_count: int

    def __init__(self):
        self.img_inf = ImageInf("untitled", "/", "none", None, 0, 0, 0)
        self.category_view = list()
        self.box_view = list()
        self.a_deviation_count = 0
        self.b_deviation_count = 0

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
