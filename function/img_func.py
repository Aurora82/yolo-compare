from function.res import Result
from PIL import Image
from math import sqrt


def img_inf_fill(res: Result, img_path: str, image_id: int):
    res.img_inf.name = str(image_id).zfill(12) + ".jpg"
    res.img_inf.path = img_path + '/' + str(res.img_inf.name)
    img = Image.open(res.img_inf.path)
    res.img_inf.size = img.size
    res.img_inf.width = img.width
    res.img_inf.height = img.height
    res.img_inf._format = img.format
    res.img_inf.diagonal = sqrt(pow(res.img_inf.width, 2) + pow(res.img_inf.height, 2))
    res.img_inf.is_fill = True
