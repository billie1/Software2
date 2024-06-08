from Component import *
from Strategy import *


# 定义叶子类 Leaf，继承自组件基类 Component
class Leaf(Component):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.icon = ""  # 图标
        self.is_first = False  # 是否为第一个
        self.is_last = False  # 是否为最后一个

    def add(self, component):
        pass

    def get_children(self):
        pass

    @abstractmethod
    def draw(self, prefix):
        pass


# 继承 Leaf 类的子类 TreeLeaf
class TreeLeaf(Leaf):
    def draw(self, prefix):
        tree_strategy = TreeStyleStrategy(self, prefix)
        tree_strategy.execute(is_leaf=True)


# 继承 Leaf 类的子类 RectangleLeaf
class RectangleLeaf(Leaf):
    def draw(self, prefix):
        rect_strategy = RectangleStyleStrategy(self, prefix)
        rect_strategy.execute(is_leaf=True)
