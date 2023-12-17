from canvas.object_canva import ObjectCanva
from canvas.object_canva import GroupElementCanva

class StageCanvas(GroupElementCanva):
    def __init__(self, name: str, parent: ObjectCanva = None):
        super().__init__(name, parent)