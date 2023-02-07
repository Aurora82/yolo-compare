import os
from collections import defaultdict


def get_fname(folder_dir):
    path = folder_dir
    files = os.listdir(path)  # Use listdir read all files in path
    files.sort()

    fname_list = []
    for file_ in files:
        if not os.path.isdir(path + file_):
            f_name = str(file_)
            fname_list.append(f_name)

    return fname_list  # Return all file's directory


def trans_to_dict(dir3):
    # Standard val
    filename_list = get_fname(dir3)

    dict_c = defaultdict(list)  # Set a default dict

    for filename in filename_list:  # Eg. 000000000139.txt in [000000000139.txt, ...]
        img_num = filename.split('.')[0]  # 000000000139
        with open(dir3 + '/' + filename) as file:  # Open 000000000139.txt
            for line in file:  # Every line for val, for example: 22 0.161641 0.711069 0.101219 0.268553
                line = line.strip('\n')  # Get rid of \n for the end of line
                sres = line.split(' ')  # Split result
                category = sres[0]
                box_cx = sres[1]
                box_cy = sres[2]
                box_w = sres[3]
                box_h = sres[4]
                val_list = [category, box_cx, box_cy, box_w, box_h]
                dict_c[int(img_num)].append(val_list)  # val_dict:{298251:[category, box_cx, box_cy, box_w, box_h]}

    return dict_c
