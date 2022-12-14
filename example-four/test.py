class Polygon():
    '''
        Class is Polygon
        functions are render and name
    '''

    def render(self):
        print("Rendering Polygon")

    def name(self, name):
        self.name = name
        print("Name: " + self.name)


class Square(Polygon):
    '''
        Class is Square but it is inherited from Polygon
        function is render but override function from parent class
    '''

    # Override
    def render(self):
        print("Rendering Square")


class Circle(Polygon):
    '''
        Class is Circle but it is inherited from Polygon
        function is name but override function from parent class
    '''

    # Override
    def name(self, name):
        self.name = name
        print("Circle name: " + self.name)


square = Square()
circle = Circle()

square.render()
circle.render()

square.name("square")
circle.name("circle")
