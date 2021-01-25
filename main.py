import pygame, sys, random


class Runner():
    __customes = ("turtle", "fish", "prawn", "moray", "octopus")
    
    def __init__(self, x=0, y=0):
        
        ixCustome = random.randint(0,4)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
        
    def avanza(self):
        self.position[0] += random.randint(1, 2)

class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ("Speedy", "Mariella", "Agus", "Silvia")
    __starLine = -5
    __finishLine = 600
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            theRunner = Runner(self.__starLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)

    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for activeRunner in self.runners:
                activeRunner.avanza()
                
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
    
            self.__screen.blit(self.__background, (0, 0))
            #self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            #self.__screen.blit(self.runners[1].custome, self.runners[1].position)
            #self.__screen.blit(self.runners[2].custome, self.runners[2].position)
            #self.__screen.blit(self.runners[3].custome, self.runners[3].position)
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
        
            pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        

    
if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()