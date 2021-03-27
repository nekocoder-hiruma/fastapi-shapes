import math

from sqlalchemy import Column, Integer

from app.models.base import BaseModel


class Triangle(BaseModel):
    __tablename__ = "Triangle"

    base = Column(Integer)
    adjacent = Column(Integer)
    opposite = Column(Integer)

    def calculate_area(self):
        half_perimeter = (self.base + self.adjacent + self.opposite) / 2
        heron_part = (half_perimeter - self.base) * (half_perimeter - self.adjacent) * (half_perimeter - self.opposite)
        return math.sqrt(half_perimeter * heron_part)

    def calculate_perimeter(self):
        return self.base + self.adjacent + self.opposite


class Square(BaseModel):
    __tablename__ = "Square"

    side = Column(Integer)

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return self.side * 4


class Rectangle(BaseModel):
    __tablename__ = "Rectangle"

    width = Column(Integer)
    length = Column(Integer)

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width * 2) + (self.height * 2)


class Diamond(BaseModel):
    __tablename__ = "Diamond"

    length = Column(Integer)
    diagonal_one = Column(Integer)
    diagonal_two = Column(Integer)

    def calculate_area(self):
        return (self.diagonal_one * self.diagonal_two) / 2

    def calculate_perimeter(self):
        return self.length * 4
