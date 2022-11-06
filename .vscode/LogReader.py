from re import T
from Gamelog import getClean, printTextList
import spacy
nlp = spacy.blank("en")
nlp2 = spacy.load("en_core_web_sm")
positions={"p","c","1b","2b","3b","ss","lf","cf","rf","p.","c.","1b.","2b.","3b.","ss.","lf.","cf.","rf."}
outPhrases = {"flied out", "fouled out","struck out swinging", "struck out swinging,","struck out looking", "struck out looking,","popped up", "grounded out", "caught stealing", "out at first", "out at second", "out at third"}
exceptions = {"reached first"}

class Player():
    def __init__(self, name):#Constructor
        self.name = name
    def __str__(self):#toString()
        return self.name

#classYear, PA,H,singles,doubles,triples,HR,BBpercent, Kpercent, HBP,batavg,SB,CS,IBB
class PositionPlayer(Player):
    def __init__(self, name):#Constructor
        self.name = name
    def __str__(self):#toString()
        return self.name
        

#classYear, handedness,team,games,IP,xERA,kper9
class Pitcher(Player):
    def __init__(self, name, ):#Constructor
        self.name = name
    def __str__(self):#toString()
        return self.name

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



def isOut(words, outphrases):
    for i in range(len(words)-2):
        if ((str(words[i])+" "+str(words[i+1]))in outphrases):#checking two words
            return True
    for i in range(len(words)-3):
        if((str(words[i]) + " " + str(words[i+1]) + " "+ str(words[i+2]))in outphrases):
            if(len(words)-i >=3):
                word1 = words[i+3]
                word2 = words[i+4]
                if((str(words[i+3])  + str(words[i+4])+" "+str(words[i+5])) == ",reached first"):
                    return False#accounting for error that happen by the catcher, maybe even 1b but haven't had that issue yet

            return True
    return False

def getInning(outs: int):
    if(outs < 6):
        return 1
    else:
        return (outs//6)+1#+1 due to 7outs//6 outs = 1 but we'd be in the second inning 

def inningOver(outs):
    if outs == 0:
        return True
    else:
        if outs%3 == 0:
            return True

def spacyRead(textList):
    outs = 0
    for i in range(len(textList)):#running through all lines - O(n)
        doc = nlp2(textList[i])#current line, only process one at a time
        
        if isOut(doc,outPhrases):#If a batter is out
            outs += 1 # we are now keeping track of outs
            print(doc)
            print("Outs:\t"+ str(outs))
            
            if(inningOver(outs)):
                print("\nInning #: " + str(getInning(outs)))
            

        for j in range(len(doc)):
            #definitely use doc[i].pos_ == PROPN to get names
            if(str(doc[j].pos_) =="PROPN" and str(doc[j].text) not in positions):
                #ISOLATED NAMES HERE -> GET THEM USING doc[i].TEXT
                token_text = doc[j].text
                token_pos = doc[j].pos_
                #print(f"{token_text:<12}{token_pos:<10}")

            

            

def addNewPlayer(Team1, Team2,token1,token2):#have to add knowing which team it is before I can add the players, keep track of the outs to do this
    if((str(token1)+" "+str(token2) ) not in (Team1, Team2)): 
        Team1.append(PositionPlayer(str(token1)+" "+str(token2)))#this line ain't right
        

textList = getClean()#textList is just the strings of the gamelogs

print("********************************************************************************\n")
#readTextList(textList)
printTextList(textList)
print("\n")
spacyRead(textList)


