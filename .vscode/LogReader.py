from re import T
from Gamelog import getClean, printTextList
import spacy
nlp = spacy.blank("en")
nlp2 = spacy.load("en_core_web_sm")
positions={"p","c","1b","2b","3b","ss","lf","cf","rf","p.","c.","1b.","2b.","3b.","ss.","lf.","cf.","rf."}

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
       





        
def indexOfABA(wordArray):#returns index of an At-Bat Action - O(n^2)
    atBatActions = {"flied out", "singled", "struck out swinging", "struck out swinging,","struck out looking", "struck out looking,","popped up","walked", "grounded out", "tripled","doubled", "hit by pitch","reached", "homered"}
    for i in range(len(wordArray)-2):#looping through words on one line
        #ADD SEMICOLON/COMMA LOGIC HERE, ACCOUNT FOR THE MULTIPLE EVENTS
        if (wordArray[i] in atBatActions or ((wordArray[i] +" "+ wordArray[i+1])in atBatActions or ((wordArray[i] +" "+ wordArray[i+1]+" "+wordArray[i+2])in atBatActions))):
            return i

def indexOfOBA(wordArray):#returns index of on-base actions
    onBaseActions = {"advanced to second", "advanced to third", "advanced to home","stole second","stole third", "stole home", "scored","out at first","out at second","out at third","no advance"}
    for i in range(len(wordArray)-2):#looping through words on one line
        #ADD SEMICOLON/COMMA LOGIC HERE, ACCOUNT FOR THE MULTIPLE EVENTS
        if (wordArray[i] in onBaseActions or ((wordArray[i] +" "+ wordArray[i+1])in onBaseActions or ((wordArray[i] +" "+ wordArray[i+1]+" "+wordArray[i+2])in onBaseActions))):
            return i
    
def indexOfSubs(wordArray):#returns index of substitution actions
    substitutionActions = {"to p for","pinch ran for", "to", "pinch hit for","to c for" ,"to 1b for", "to 2b for", "to ss for", "to 3b for", "to lf for", "to cf for", "to rf for"}
    for i in range(len(wordArray)-2):#looping through words on one line
        #ADD SEMICOLON/COMMA LOGIC HERE, ACCOUNT FOR THE MULTIPLE EVENTS
        if (wordArray[i] in substitutionActions or ((wordArray[i] +" "+ wordArray[i+1]+" "+wordArray[i+2])in substitutionActions)):#only 1 and 3 words are checked so only need to check for those combos
            return i
    

def findNameABA(actionIndex: int, words, names):#finds name given an array of words and an index of the At-Bat action
    if actionIndex == 2:
        name = words[0] + " " + words[1]
        #print(words[2])
    else:
        name = words[0]
        #print(words[1])
    return name

def findNameOBA(actionIndex: int, words, names):#finds name given an array of words and an index of the At-Bat action
    #gonna need to account for every 
    if actionIndex == 2:
        name = words[0] + " " + words[1]
        #print(words[2])
    else:
        name = words[0]
        #print(words[1])
    return name
        
def spacyRead(textList):
    for i in range(len(textList)):#running through all lines - O(n)
        doc = nlp2(textList[i])
        for token in doc:
            #definitely use token.pos_ == PROPN to get names
            if(str(token.pos_) =="PROPN" and str(token.text) not in positions):
                token_text = token.text
                token_pos = token.pos_
                print(f"{token_text:<12}{token_pos:<10}")    
            
            

        

textList = getClean()#textList is just the strings of the gamelogs
#readTextList(textList)
printTextList(textList)
spacyRead(textList)


