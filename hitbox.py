class Hitbox:
    def __init__(self,x,y,width,height):
        self.__x = x
        self.__y = y
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return f'__x={self.__x} __y={self.__y} __width={self.__widht} __height={self.__height}'

    def __get_widht(self):
        return self.__widht
    def __set_width(self,width):
        if width < 0:
            width = -width
        self.__widht = width

    def ___get_height(self):
        return self.__height
    def __set_height(self,height):
        if height < 0:
            height = -height
        self.__height = height

    def __get_x(self):
        return self.__x
    def __set_x(self,x):
            self._x = x

    def __get_y(self):
        return self.__y
    def __set_y(self,y):
            self._y = y

    def moveto(self,x,y):
        self.__set_x(x)
        self.__set_y(y)

    x = property(__get_x,__set_x)
    y = property(__get_y,__set_y)
    width = property(__get_widht,__set_width)
    height = property(___get_height,__set_height)