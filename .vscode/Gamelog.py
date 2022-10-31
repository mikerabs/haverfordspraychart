def fetchHTML():
    import requests

    url = "https://stats.ncaa.org/game/play_by_play/5215900"

    payload={}
    headers = {
    'authority': 'stats.ncaa.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_stats_session=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiJTFjNWI1ZWYxNmQ4NGIyMDU0MDhmOTE0YTJkNDdiYjk4BjsAVEkiF2xpdmVzdHJlYW1fdXNlcl9pZAY7AEZJIjEwdVlGbkNEbG1DUENlQUZvUUNHY0lobnljUnJ4dFdhaGljYWJlTGNxaDdjdAY7AEZJIhBfY3NyZl90b2tlbgY7AEZJIjEvT0FrcGMvanI2UkZ1SDlvd0ZqUUxZYWZyUVRXMlhtNHpSbGJUUDN4d25RPQY7AEY%3D--e45fbb36da1ffe795ad809471ef99ed099a27cdc; AKA_A2=A; RT="z=1&dm=ncaa.org&si=x10310tdwo&ss=l9st9yt3&sl=0&tt=0"; X-Oracle-BMC-LBS-Route=e0e8f5ccc6c39fedaa6765ef3ac329941e557d93',
    'if-none-match': 'W/"b108c7e372117eae862d0965e4979a49"',
    'referer': 'https://stats.ncaa.org/game/period_stats/5215900',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    #print(response.text)

    return response.text

def SoupNav(htmldata):    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(htmldata)
    tables = soup.findAll('table',{'class': 'mytable'},width = "1000px",)
    return tables

def numberOfTables(tables):
    count = 0
    for table in tables:
        count +=1
    return count

def findTextFromTable(data,tableNum, htmlelement,  identifier):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data)

    text = soup.find_all(htmlelement,identifier)
    
    return text

def printTextList(textList):
    for i in textList:
        print(i)


def makeStringList(textList):
    for i in range(len(textList)):#turn html data into strings
        textList[i] = str(textList[i])
    return textList


def cleanTextList(textList):
    #working now don't fuck it up
    i = 0
    lengthTextList = len(textList)
    countSM = 0#counts how many are deleted
    countAlign = 0
    countTD1 = 0
    countTD2 = 0
    while (i < lengthTextList):
        if(textList[i] == ("<td class=" + '"smtext"' + "></td>")):
            textList.pop(i)
            #print("deleted smtexts")
            countSM+=1
            lengthTextList = len(textList)
            continue
        if(textList[i][0:8]=="<td alig"):#gets rid of the aligns
            textList.pop(i)
            #print("deleted align")
            countAlign+=1
            lengthTextList = len(textList)
            continue

        if(textList[i][(len(textList[i])-6):len(textList[i])+1]== "></td>"):#parsing out the extra tds
            textList.pop(i)
            #print("deleted ><")
            countTD1+=1
            lengthTextList = len(textList)
            continue
    
        if(textList[i][(len(textList[i])-6):len(textList[i])+1]== "0</td>"):#parsing out the extra tds
            textList.pop(i)
            #print("deleted 0<")
            countTD2+=1
            lengthTextList = len(textList)
            continue
        i+=1

    for j in range(len(textList)):# deleting the html tags from front and back
        textList[j] = textList[j][19: len(textList[j])-5]

    #print("\n\nAfter cleaning . . .\n"+ str(countSM)+ " deleted smtexts\n"+ str(countAlign)+" deleted aligns\n"+ str(countTD1)+" deleted ><s\n"+ str(countTD2)+" deleted 0<s\n")    
    
    return textList





def getClean():
    htmldata = fetchHTML()
    tables = SoupNav(htmldata)
    text = findTextFromTable(htmldata, 0, 'td', {'class':'smtext'})
    textList = makeStringList(text)

    return cleanTextList(textList)


#printTextList(getClean())
