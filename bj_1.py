import random as rd
import pygame

card = [2,3,4,5,6,7,8,9,10,"A",'K','Q','J']

class blackjack():
    def __init__(self, dealermoney,mymoney):
        self.dealer = 0
        self.me = 0
        self.my_res =""
        self.dealer_res = ""
        self.game_res = ""

        self.msg=""

        self.issplit = False

        #dealer win, you win, dealer blackjack, your blackjack, push, num of game
        self.board = [0,0,0,0,0,0]

        self.my_money=mymoney
        self.dealer_money = dealermoney

    def dealer_turn(self):
        while(self.dealer<=16):
            self.dealer_card.append(self.getcard())
            self.dealer = self.cal_card(self.dealer_card)
        
        if self.dealer==21:
            self.dealer_res = "black jack"
            self.board[2]+=1
        elif self.dealer >21:
            self.dealer_res = "burst"

        if self.issplit:
            self.show(self.my1_res, self.money1)
            self.show(self.my2_res, self.money2)
        else: 
            self.show(self.my_res, self.money)
        self.displaying(show=True)

    def getcard(self):
        num = rd.randrange(9999) %14
        return card[num]

    def start(self, money):
        self.dealer = 0
        self.dealer_card = []
        self.me = 0
        self.my_card = []
        self.my_res =""
        self.dealer_res = ""
        self.game_res = ""
        self.issplit = False

        self.money = money

        self.board[5]+=1
        self.dealer_card.append(self.getcard())
        self.dealer = self.cal_card(self.dealer_card)
        self.dealer_card.append(self.getcard())
        self.dealer = self.cal_card(self.dealer_card)
        self.my_card.append(self.getcard())
        self.me = self.cal_card(self.my_card)
        self.my_card.append(self.getcard())
        self.me = self.cal_card(self.my_card)

    def start2(self):
        if self.my_card[0]==self.my_card[1] :
            ch = self.get_input("you can choose split")
            if ch=="4":
                self.split(self.my_card[0])
            else: self.select()
        elif self.me < 21 :
            self.select()
        else:
            self.my_res = "black jack"
            self.board[3]+=1
            self.dealer_turn()

    def show(self, my_res, money):
        if my_res==self.dealer_res:
            if my_res=="":
                if self.me>self.dealer:
                    self.game_res = "you win"
                    self.board[1]+=1
                elif self.me<self.dealer:
                    self.game_res = "dealer win"
                    self.board[0]+=1
                else:
                    self.game_res = "push"
                    self.board[4]+=1
            else:
                self.game_res = "push"
                self.board[4]+=1
        elif my_res == "black jack":
            self.game_res = "you win"
            self.board[1]+=1
        elif self.dealer_res == "black jack":
            self.game_res = "dealer win"
            self.board[0]+=1
        else:
            if my_res=="burst":
                self.game_res = "dealer win"
                self.board[0]+=1
            else:
                self.game_res = "you win"
                self.board[1]+=1
        self.cal_money(money)

    def cal_money(self,money):
        if self.game_res == "you win":
            self.my_money+=money
            self.dealer_money-=money
        elif self.game_res == "dealer win":
            self.dealer_money+=money
            self.my_money-=money
    
    def select(self):

        ch = self.get_input("select")
        self.displaying()
        #input("hit:1 stand:2 double down:3")
        if (ch=="3"):
            self.money=self.money*2
            self.displaying()
        while(ch!="2"):
            self.my_card.append(self.getcard())
            self.me = self.cal_card(self.my_card)
            self.displaying()
            if(self.me==21):
                self.my_res="black jack"
                self.board[3]+=1
                self.displaying()
                return self.dealer_turn()
            elif (self.me>21):
                self.my_res="burst"
                self.displaying()
                return self.dealer_turn()
            elif (ch=="1"):
                ch = self.get_input("select")
            else : 
                break
        self.displaying()
        self.dealer_turn()
    
    def cal_card(self, cards):
        tmp=0
        tmp_card=[]
        for j in cards:
            if j=="K" or j=="Q" or j=="J":
                tmp_card.append(10)
            elif j=="A":
                tmp_card.append(11)
            else:
                tmp_card.append(j)
        tmp_card = sorted(tmp_card)
        for i in tmp_card:
            if i==11:
                if tmp>10:
                    tmp+=1
                else:
                    tmp+=11
            else:
                tmp+=i

        return tmp

    def split(self, num):

        self.me1_card = [num]
        self.me2_card = [num]
        self.money1 = self.money
        self.money2 = self.money
        self.me1 = self.cal_card(self.me1_card)
        self.me2 = self.cal_card(self.me2_card)
        self.my1_res = ""
        self.my2_res = ""


        self.issplit=True

        ch = self.get_input("select")
        if (ch=="3"):
            self.money1=self.money*2
        while(ch!="2"):
            self.me1_card.append(self.getcard())
            self.me1 = self.cal_card(self.me1_card)
            
            if(self.me1==21):
                self.my1_res="black jack"
                self.board[3]+=1
                break
            elif (self.me1>21):
                self.my1_res="burst"
                break
            elif (ch=="1"):
                ch = self.get_input("select")
            else : 
                break
        
        ch = self.get_input("select")
        if (ch=="3"):
            self.money2=self.money*2
        while(ch!="2"):
            self.me2_card.append(self.getcard())
            self.me2 = self.cal_card(self.me2_card)
            if(self.me2==21):
                self.my2_res="black jack"
                self.board[3]+=1
                break
            elif (self.me2>21):
                self.my2_res="burst"
                break
            elif (ch=="1"):
                ch = self.get_input("select")
            else : 
                break
        

        self.dealer_turn()

    def get_input(self,msg):
        self.displaying(msg)
        while(1):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if 550>mouse[0]>400 and 675>mouse[1]>625 :
                    if click[0] : 
                        return "3"
                if 750>mouse[0]>600 and 675>mouse[1]>625 :
                    if click[0] : 
                        return "4"
                if 950>mouse[0]>800 and 675>mouse[1]>625 :
                    if click[0] : 
                        return "2"
                if 1150>mouse[0]>1000 and 675>mouse[1]>625 :
                    if click[0] : 
                        return "1"
                        
    def displaying(self, msg="",show=False):
        screen.fill((000,102,000))
        printText(self.dealer_money, pos=(135,130), font=font15)
        printText(self.my_money, pos=(135,175), font=font15)
        printText(self.money,pos =(135,220), font=font15)
        screen.blit(moneyImg,(50,50))
            
            
        screen.blit(resImg,(50,300))


        screen.blit(doubleImg,(400,625))
        screen.blit(splitImg,(600,625))
        screen.blit(standImg,(800,625))
        screen.blit(hitImg,(1000,625))
        printText(msg,pos=(550,300))

        if show:
            printText(self.dealer_res  , pos = (130,380), font=font15)
            printText(self.dealer_card, pos=(600,100))
            printText(self.dealer,pos=(550, 100))
        else:
            printText(self.dealer_card[0], pos=(600,100))

        if self.issplit:
            printText(self.me1_card,pos=(600, 500))
            printText(self.me2_card,pos=(600, 550))
            printText(self.me1,pos=(550, 500))
            printText(self.me2,pos=(550, 550))

            printText(self.my1_res,pos=(450,500))
            printText(self.my2_res,pos=(450,550))
        else: 
            printText(self.my_card,pos=(600, 525))
            printText(self.me,pos=(550, 525))
            printText(self.my_res , pos = (130,425), font=font15)
            printText(self.game_res , pos = (130,470), font=font15)

        pygame.display.flip()  







standImg = pygame.image.load("stand.png")
doubleImg = pygame.image.load("double.png")
hitImg = pygame.image.load("hit.png")
splitImg = pygame.image.load("split.png")
moneyImg = pygame.image.load("money.png")
resImg = pygame.image.load("result.png")
logoImg = pygame.image.load("logo.png")


pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
pygame.display.set_caption("Black Jack")
screen.fill((000,102,000))
font15 = pygame.font.SysFont("consolas", 15)
font20 = pygame.font.SysFont("consolas", 20)
pygame.display.set_icon(logoImg)

start = False
inGame=False


def printText(msg, color='BLACK', pos=(50, 50), font=font20):
    textSurface      = font.render(str(msg), True, pygame.Color(color), None)
    textRect         = textSurface.get_rect()
    textRect.topleft = pos
 
    screen.blit(textSurface, textRect)

def typing(msg1, msg2):
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(msg2)>0:
                        msg2=msg2[:-1]
                elif event.key == pygame.K_SPACE:
                    return int(msg2)
                else :
                    msg2+=event.unicode
            screen.fill((000,102,000))
            printText(msg1,pos=(500,200))
            printText("press space bar if ended", pos=(500,250))
            printText(msg2,pos=(500,350))
        pygame.display.flip()  

def gameStart():
    
    screen.fill((000,102,000))
    dealerMoney = typing("input dealer's money","")
    mymoney = typing("input your money","")

    inGame = True
    game = blackjack(dealerMoney,mymoney)
    while(inGame): 
        screen.fill((000,102,000))
        money = typing("input betting money", "")
        game.start(money)
        game.displaying()
        game.start2()

        loop=True
        while(loop):
            screen.fill((000,102,000))
            game.displaying("continue? (y/n)", show=True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        loop=False

                    if event.key == pygame.K_n:
                        return [game.dealer_money-dealerMoney,game.my_money-mymoney,
                        game.board[0],game.board[1],game.board[4],game.board[2],game.board[3],game.board[5]]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN:
            start = True

    if start == True:
        a,b,c,d,e,f,g,h = gameStart()
        while(1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            screen.fill((000,102,000))
            printText("| result | ",pos=(600,100))  
            printText("dealer get money : ", pos=(400,250))
            printText("you get money : ", pos=(400,300))
            printText("number of dealer win: ", pos=(400,350))
            printText("number of you win : ", pos=(400,400))
            printText("number of push : ", pos=(400,450))
            printText("number of dealer blackjack : ", pos=(400,500))
            printText("number of your blackjack : ", pos=(400,550))
            printText("number of game : ", pos=(400,600))

            printText(a, pos=(900,250))
            printText(b, pos=(900,300))
            printText(c, pos=(900,350))
            printText(d, pos=(900,400))
            printText(e, pos=(900,450))
            printText(f, pos=(900,500))
            printText(g, pos=(900,550))
            printText(h, pos=(900,600))
            pygame.display.flip()  
    else:
        printText("press any key", pos=(550,300))

    pygame.display.flip()  
    clock.tick(60)         