import geoformulas

responses = [
    {'reply':"Well you see I don't have a name",'requirements':['what'],'must':['name'],'probability':0},
    {'reply':"I am doing fine",'requirements':['how'],'must':["are",'you'],'probability':0},
    {'reply':"Bye!! see you around",'requirements':[],'must':['bye'],'probability':0},
    {'reply':"My name is Chat Bot",'requirements':[],'must':['thanks','thank','thankyou'],'probability':0},


    {'reply':geoformulas.areaOfSquare,'requirements':['find'],'must':['area','square'],'hasArg':True,'probability':0},
    {'reply':geoformulas.perimeterOfSquare,'requirements':['find'],'must':['perimeter','square'],'hasArg':True,'probability':0},
]

def getProbability(wordlist):
    tempMark = 0
    for x in responses:
        for y in wordlist:
            if y in x['requirements']:
                tempMark += 5
            if y in x['must']:
                tempMark += 10
        x['probability'] = tempMark
        tempMark = 0

def getResponce():
    index = 0
    temphigh = 0

    arguments = {}
    flag = False
    arg = ""

    for x in inp.split(" "):
        if flag:
            number = ""
            for y in str(x):
                if y in ['1','2','3','4','5','6','7','8','9','0']:
                    number = number + y
            arguments[arg] = int(number)
            flag = False
        else:
            if x in ['base','height','length','radius','side','breadth']:
                arg = x
                flag = True

    for x in range(len(responses)):
        if temphigh < responses[x]['probability']:
            index = x
            temphigh = responses[x]['probability']

    if responses[index]['hasArg'] == True and len(arguments.keys()) > 0:
        return(responses[index]['reply'](arguments))
    else:
        return(responses[index]['reply'])

while True:
    global inp 
    inp = input("User: ")
    getProbability(inp.split(" "))
    print("Bot: "+getResponce() + "\n")


