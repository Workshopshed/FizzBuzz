from time import sleep
import sys,pygame

class FizzBuzz:
    """Fizz Buzz Game"""
    startMsg = 'Fizz Buzz - Press space to continue'
    running = True
    delayS = 1
    keyState = {'fizz': False, 'buzz': False}
    
    screen = {}

    def quit(self):
        print('Shutting down')
        pygame.quit()
        sys.exit()

    def waitForPress(self):
        print('Waiting for key press')
        pygame.event.clear()
        x = False
        while x == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    if event.key == pygame.K_SPACE:
                        x = True

    def checkKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    self.keyState['fizz'] = True
                    self.print("User selected Fizz",(60,130))
                if event.key == pygame.K_b:
                    self.keyState['buzz'] = True
                    self.print("User selected Buzz",(60,150))

    def resetKeys(self):
        self.keyState = {'fizz': False, 'buzz': False}

    def pause(self,delay):
        for x in range(0, 9):
           self.checkKeys()
           sleep(delay / 10)

    def print(self,text,position,fontSize=12):
        print(text)
        f=pygame.font.SysFont("arial",fontSize)
        text1=f.render(text,True,(255,255,255))
        self.screen.blit(text1,position)
        pygame.display.update()

    def printNumber(self,number):
        #Blank number
        pygame.draw.rect(self.screen,(0,0,0),(60,100,20*len(str(number)),20))
        #Blank fizbuzz
        pygame.draw.rect(self.screen,(0,0,0),(60,130,120,80))
        self.print(str(number), (60,100),20)

    def initDisplay(self):
        pygame.init()
        size = (700, 500)
        self.screen = pygame.display.set_mode(size)
        
    def start(self):
        self.initDisplay();
        self.print(self.startMsg,(60,60))
        self.waitForPress()
        self.print('Off we go', (60,80))
        self.pause(0.5)

    def checkFizzBuzz(self,number):
        if (number % 3 == 0 and number % 5 == 0):
            self.print("FizzBuzz",(60,170))
            if self.keyState['fizz'] != True and self.keyState['buzz'] != True:
                self.running = False
        elif (number % 3 == 0):
            self.print("Fizz",(60,170))
            if self.keyState['fizz'] != True:
                self.running = False
        elif (number % 5 == 0):
            self.print("Buzz",(60,190))
            if self.keyState['buzz'] != True:
                self.running = False
        elif (self.keyState['fizz'] == True or self.keyState['buzz'] == True):
                self.running = False

    def run(self):
        self.start()

        counter = 1
        while self.running:
            self.printNumber(counter)
            self.pause(self.delayS)
            self.checkFizzBuzz(counter)
            sleep(0.5)
            self.resetKeys()
            counter += 1
        #Todo: End Game
        print('Game Over')

app = FizzBuzz()
app.run()


