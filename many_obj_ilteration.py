class baba:
    area=85
    age=75
    def __init__(self):
        print("baba ki pass")
        
class papa(baba):
    area=85
    age=45
    def __init__(self):
        print("papa ki pass")
class beta(papa):
    area=10000
    age=20
    def __init__(self):
        super().__init__()
        print("beta ki pass")
