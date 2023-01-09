class Box:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def StringifyBox(self):
        return f'Left is: {self.left}\nTop is: {self.top}\nWidth is: {self.width}\nHeight is: {self.height}'
