class Board:
    def __init__(self):
        self.A1 = None
        self.A2 = None
        self.A3 = None
        self.B1 = None
        self.B2 = None
        self.B3 = None
        self.C1 = None
        self.C2 = None
        self.C3 = None
        self.D1 = None
        self.D2 = None
        self.D3 = None
        self.E1 = None
        self.E2 = None
        self.E3 = None

    def GetAllTiles(self):
        tiles = [
            self.A1,
            self.A2,
            self.A3,
            self.B1,
            self.B2,
            self.B3,
            self.C1,
            self.C2,
            self.C3,
            self.D1,
            self.D2,
            self.D3,
            self.E1,
            self.E2,
            self.E3
        ]
        return tiles
