import pickle

from function import pred_func
from function import val_func
from function import category_analyse
from function import box_analyse
from function import img_func
from classes.res import Result
from classes.server import Server


def pre_func():
    server = Server()
    socket = server.listen_socket()
    data = []
    picket = socket.recv(server.BUFFLEN)
    data.append(picket)
    para = pickle.loads(b"".join(data))
    print(para)
    dir1 = para.yolo_imp_file_path
    dir2 = para.yolo_file_path
    dir3 = para.standard_val_dir_path
    dir4 = para.img_dir_path
    deviation = para.deviation
    dict_a, dict_b, dict_c = read_from_file(dir1, dir2, dir3)
    keys = dict_c.keys()
    count = 0
    for _key in keys:
        res = compare(dict_a, dict_b, dict_c, dir4, _key, deviation)
        socket.send(pickle.dumps(res))
        count += 1
        if count > 3:
            break
    socket.close()


def compare(dict_a, dict_b, dict_c, img_dir, _key, deviation):
    print("_key: ", _key)  # "139": [["58", "0.389578", "0.416103", "0.038594", "0.163146"],...]
    res = Result()  # Result
    res.image_id = _key  # 139
    res.img_path = img_dir  #
    img_func.img_inf_fill(res, res.img_path, res.image_id)
    box_analyse.uniformize(res, dict_a, dict_b)
    category_analyse.analyse(res, dict_a, dict_b, dict_c, res.image_id)
    box_analyse.analyse(res, dict_a, dict_b, dict_c, res.image_id, deviation)
    return res


def read_from_file(dir1, dir2, dir3):
    dict_a = pred_func.json_read(dir1)  # YOLO improvement
    dict_b = pred_func.json_read(dir2)  # YOLO
    dict_c = val_func.trans_to_dict(dir3)  # Standard val
    return dict_a, dict_b, dict_c
