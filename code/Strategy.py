from abc import ABC, abstractmethod


# 抽象策略类，定义了风格策略的接口
class StyleStrategy(ABC):
    @abstractmethod
    def execute(self, is_leaf):
        """执行绘制操作，根据节点类型选择绘制方法"""
        pass

    @abstractmethod
    def draw_container(self):
        """绘制容器节点"""
        pass

    @abstractmethod
    def draw_leaf(self):
        """绘制叶子节点"""
        pass


# 树形风格策略类
class TreeStyleStrategy(StyleStrategy):
    def __init__(self, node, prefix):
        self.node = node  # 当前节点
        self.prefix = prefix  # 前缀，用于层次表示

    def execute(self, is_leaf):
        """根据节点类型调用相应的绘制方法"""
        if is_leaf:
            self.draw_leaf()
        else:
            self.draw_container()

    def draw_container(self):
        """绘制容器节点"""
        print(self.prefix + ("└─" + self.node.icon if self.node.is_last else "├─" + self.node.icon) + self.node.name)
        new_prefix = self.prefix + ("    " if self.node.is_last else "│   ")
        iterator = self.node.create_iterator()
        while iterator.has_next():
            child = iterator.next()
            child.is_last = not iterator.has_next()  # 判断是否是最后一个子节点
            child.draw(new_prefix)  # 递归绘制子节点

    def draw_leaf(self):
        """绘制叶子节点"""
        print(self.prefix + ("└─" + self.node.icon if self.node.is_last else "├─" + self.node.icon)
              + f"{self.node.name}: {self.node.value}")


# 矩形风格策略类
class RectangleStyleStrategy(StyleStrategy):
    def __init__(self, node, prefix):
        self.node = node  # 当前节点
        self.prefix = prefix  # 前缀，用于层次表示

    def execute(self, is_leaf):
        """根据节点类型调用相应的绘制方法"""
        if is_leaf:
            self.draw_leaf()
        else:
            self.draw_container()

    def draw_container(self):
        """绘制容器节点"""
        if self.node.is_first:
            print(self.prefix + "┌─" + self.node.icon + self.node.name + "─" *
                  (40 - len(self.prefix) - len(self.node.name)) + "┐")
        else:
            print(self.prefix + "├─" + self.node.icon + self.node.name + "─" *
                  (40 - len(self.prefix) - len(self.node.name)) + "┤")

        iterator = self.node.create_iterator()
        while iterator.has_next():
            child = iterator.next()
            new_prefix = self.prefix + "│  " if not child.is_last else self.prefix + "└──"
            child.draw(new_prefix)  # 递归绘制子节点

    def draw_leaf(self):
        """绘制叶子节点"""
        if self.node.is_last:
            print(self.prefix + "┴─" + self.node.icon + f"{self.node.name}: {self.node.value} "
                  + "─" * (37 - len(self.prefix) - len(self.node.name) - len(str(self.node.value))) + "┘")
        else:
            print(self.prefix + "├─" + self.node.icon + f"{self.node.name}: {self.node.value} "
                  + "─" * (37 - len(self.prefix) - len(self.node.name) - len(str(self.node.value))) + "┤")
