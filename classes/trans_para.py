import json


class Parameters:
    yolo_imp_file_path: str
    yolo_file_path: str
    standard_val_dir_path: str
    img_dir_path: str
    deviation: float

    def __init__(self):
        self.yolo_imp_file_path = ''
        self.yolo_file_path = ''
        self.standard_val_dir_path = ''
        self.img_dir_path = ''
        self.deviation = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.__str__()
