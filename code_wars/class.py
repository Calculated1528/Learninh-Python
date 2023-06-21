class Car: 
    def move(self):
        print("Car is moving")
    
    def stop(self):
        print("Car stoped")

my_car = Car()
print(dir(my_car))
print(isinstance(my_car, Car))

my_car.move()


## __init__ создаёт собственные атрибуты у экземпляров классов

class Comment: 
    def __init__(self, text, inital_votes_qty=0):
        self.text = text
        self.votes_qty = inital_votes_qty

    def upvote(self, qty):
        self.votes_qty += qty

    def reset_votes_qty (self):
        self.votes_qty = 0

my_comment = Comment("First comment")



## Задание на классы 172 видео

class Image:
    def __init__(self, text, size, inital_size=0):
        self.title = text
        self.resolution = inital_size
        self.extension = size 
    
    def resize(self):
        self.resolution = 0 

