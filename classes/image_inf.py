import json
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
