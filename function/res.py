import json


class CategoryView:
    # -1 stand for not found.
    standard_category: int  # standard category id
    standard_category_box_amount: int  # Amount of box in each standard category
    a_category: int  # A category id
    a_category_miss_amount: int  # The amount of not match with standard category
    a_category_box_amount: int  # Amount of box in each A's category

    b_category: int  # B category id
    b_category_miss_amount: int  # The amount of not match with standard category
    b_category_box_amount: int  # Amount of box in each B's category

    def __init__(self):
        self.a_category_miss_amount = 0
        self.b_category_miss_amount = 0

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


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


class ImageInf:
    name: str
    path: str
    _format: str
    size: tuple
    width: int
    height: int
    diagonal: float
    is_fill: bool

    def __init__(self, name, path, _format, size, width, height, diagonal):
        self.name = name
        self.path = path
        self._format = _format
        self.size = size
        self.width = width
        self.height = height
        self.diagonal = diagonal
        self.is_fill = False

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()


class Result:
    image_id: int
    img_path: str
    img_inf: ImageInf

    category_view: list
    standard_category_amount: int
    a_category_amount: int
    b_category_amount: int

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
        self.image_id = 0
        self.img_path = ''
        self.img_inf = ImageInf("untitled", "/", "none", None, 0, 0, 0)
        self.category_view = list()
        self.standard_category_amount = 0
        self.a_category_amount = 0
        self.b_category_amount = 0
        self.a_category_coverage_rate = 0
        self.b_category_coverage_rate = 0
        self.box_view = list()
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
