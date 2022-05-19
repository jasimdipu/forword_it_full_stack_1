from abc import ABC, abstractmethod


class Student(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def getDept(self):
        return self.dept

    @abstractmethod
    def setDept(self, dept):
        pass
