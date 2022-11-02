from Gamelog import getClean, printTextList

class Player():
    def __init__(self, name, classYear):#Constructor
        self.name = name
        self.classYear = classYear
    def __str__(self):#toString()
        return self.name


class PositionPlayer(Player):
    def __init__(self, name, classYear, PA,H,singles,doubles,triples,HR,BBpercent, Kpercent, HBP,batavg,SB,CS,IBB):#Constructor
        self.name = name
        self.classYear = classYear
        self.PA = PA
        self.H = H
        self.singles = singles
        self.doubles = doubles
        self.triples = triples
        self.HR = HR
        self.BBpercent = BBpercent
        self.Kpercent = Kpercent
        self.HBP = HBP
        self.batavg = batavg
        self.SB = SB
        self.CS = CS
        self.IBB = IBB


class Pitcher(Player):
    def __init__(self, name, classYear, handedness,team,games,IP,xERA,kper9):#Constructor
        self.name = name
        self.classYear = classYear
        self.handedness = handedness
        self.team = team
        self.games = games
        self.IP = IP
        self.xERA = xERA
        self.kper9 = kper9

def readTextList(textList):
    Team1 = []
    Team2 = []

    for i in range(len(textList)):#running through all lines - O(n)
        words = textList[i].split(" ")#create temp array words to handle all words of each line
        #Lapczynski exception, have to find first instance of an action that the player did to define the player name
        
        actionIndex = indexOfABA(words)#returns starting index of position of the action
        name = findName(actionIndex,words)
        print(name)
       
        
        
def indexOfABA(wordArray):#O(n^2)
    atBatActions = {"flied out", "singled", "struck out swinging", "struck out swinging,","struck out looking", "struck out looking,","popped up","walked", "grounded out", "tripled","doubled", "hit by pitch","reached", "homered"}
    for i in range(len(wordArray)-2):#looping through words on one line
        if (wordArray[i] in atBatActions or ((wordArray[i] +" "+ wordArray[i+1])in atBatActions or ((wordArray[i] +" "+ wordArray[i+1]+" "+wordArray[i+2])in atBatActions))):
            return i
              
def findName(actionIndex: int, words):#finds name given an array of words and an index of the action
    if actionIndex == 2:
        name = words[0] + " " + words[1]
        #print(words[2])
    else:
        name = words[0]
        #print(words[1])
    return name

        


textList = getClean()#textList is just the strings of the gamelogs
#readTextList(textList)
printTextList(textList)



