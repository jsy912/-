class Point :
    def __init__(self, x=0, y=0) :
        self.__x = x
        self.__y = y

    def show(self) :
        print(f'({self.__x},{self.__y})')

    def set(self, x, y) :
        self.__x = x
        self.__y = y
    
    def get(self):
        return self.__x, self.__y
    
class Rectangle :
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0) :
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        lt = Point(x1, y1)
        rb = Point(x2, y2)

    def show(self) :
        print(f'좌측 상단 꼭지점이 ({self.__x1},{self.__y1})이고 우측 하단 꼭지점이 ({self.__x2},{self.__y2})인 사각형입니다.', end='')

    def getWidth(self):
        result = self.__x2 - self.__x1
        return result
    
    def getHeight(self):
        result = self.__y2 - self.__y1
        return result
    
    def getArea(self):
        w = self.getWidth() * self.getHeight()
        return w
    
    def getPerimeter(self):
        r = 2 * ( self.getWidth() + self.getHeight() )
        return r
    
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')