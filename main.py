class Student:
    def __init__(self,name:str="",age:int=0,score:int=0):
        self._name:str = name
        self._age:int = age
        self._score:int = score
        self._tracks:list = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
    def change_name(self,value):
        #call setter
        self.name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age = value
    def change_age(self,value):
        #call setter
        self.age = value
    @property
    def score(self):
        return self._score
    def get_score(self):
        return self.score
    @score.setter
    def score(self,value):
        self._score = value
    @property
    def tracks(self):
        return self._tracks
    @tracks.setter
    def tracks(self,value):
        self._tracks.append(value)
    def add_track(self,value):
        self.tracks.append(value)
bobby = Student(name="Bobby",age=33,score=99)
bobby.change_name("John")
print(bobby.name)
bobby.change_age(40)
print(bobby.age)
print(bobby.get_score())
bobby.add_track("UI/UX")
print(bobby.tracks)