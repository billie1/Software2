from abc import ABC, abstractmethod


# 抽象迭代器类，定义了迭代器接口
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        """检查是否还有下一个元素"""
        pass

    @abstractmethod
    def next(self):
        """返回下一个元素"""
        pass


# 具体迭代器类，用于遍历组件
class ComponentIterator(Iterator):
    def __init__(self, components):
        self._components = components  # 保存要遍历的组件列表
        self._index = 0  # 初始化索引为0

    def has_next(self):
        """检查是否还有未遍历的元素"""
        return self._index < len(self._components)

    def next(self):
        """返回下一个元素，如果没有更多元素则抛出StopIteration异常"""
        if self.has_next():
            component = self._components[self._index]  # 获取当前索引位置的组件
            self._index += 1  # 索引加1，指向下一个元素
            return component
        else:
            raise StopIteration  # 如果没有更多元素，抛出StopIteration异常
