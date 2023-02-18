import json


class CategoryView:
    # -1 stand for not found.
    standard_category: int  # standard category id
    standard_category_box_amount: int  # Amount of box in each standard category
    a_category: int  # A category id

    a_category_box_amount: int  # Amount of box in each A's category

    b_category: int  # B category id

    b_category_box_amount: int  # Amount of box in each B's category

    def __init__(self):
        self.a_category_miss_amount = 0
        self.b_category_miss_amount = 0

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
