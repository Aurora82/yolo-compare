import time

from PySide6.QtCore import QThread, QObject, Signal, Slot
from function.analyse import compare
from function import analyse
from classes.res import Result


class DataAnalyse(QObject):
    finished = Signal()
    result = Signal(Result)
    para = None

    def run(self):
        dict_a, dict_b, dict_c = analyse.read_from_file(self.para.yolo_imp_file_path,
                                                        self.para.yolo_file_path,
                                                        self.para.standard_val_dir_path)
        keys = dict_c.keys()
        count = 0
        for _key in keys:
            res = compare(dict_a, dict_b, dict_c, self.para.img_dir_path, _key, self.para.deviation)
            self.result.emit(res)
            if count > 10:
                break
            count += 1
        self.finished.emit()
