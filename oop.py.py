''' tarife class box'''
sides = [1, 2, 3, 4, 5, 6] 
class Box :
    def __init__ (self, length, width, height):
        self.length = length 
        self.width = width 
        self.height = height
        
        
class dice(Box):
    def __init__ (self, sides):
        super().__init__(lenght = 1, width = 1, height = 1)
        self.sides = sides 
        
        
    '''10 other class with inheritance '''
'''class dice1(dice):
    def __init__(self, color,glassy,unglassy ,sides ):
        super() .__init__(color)
        super() .__init__(glassy)
         super() .__init__(unglassy)
        self.sides =sides
        
        
    #creat 10 dice with diffrent colors
    dice_list=[dice("red",6)], dice [("blue",6)] ,dice [("green",6)],dice ["yellow",6]
        dice["pink",6],dice[("white",6)],dice[("gray",6)],dice[("black,6")],dice[("glassy"),6]
        dice[("unglassy",6)]  
        
        #running test
    def print_info(self)
        print("color","side")
            '''