import requests, json, pprint
from bs4 import BeautifulSoup

# awbNumber = 'FMPC0278112092'



def getJSONData(awbNumber):
    doc = requests.get('https://portal.ekartlogistics.com/track/' + awbNumber + '/')
    soup = BeautifulSoup(doc.content, 'html.parser')


    date = soup.find_all(attrs={"data-title": "Date"})
    time = soup.find_all(attrs={"data-title": "Time"})
    place = soup.find_all(attrs={"data-title": "Place"})
    status = soup.find_all(attrs={"data-title": "Status"})

    myList = []
    for i in range(len(date)):
        templist = [
            date[i].text,
            time[i].text,
            place[i].text,
            status[i].text
        ]
        myList.append(templist)

    userGets = []

    # if(order=='ascend'):
    #     for k in range(len(myList)):
    #             tempdict = {
    #                 'date': myList[k][0],
    #                 'time': myList[k][1],
    #                 'place': myList[k][2],
    #                 'status': myList[k][3]
    #             }
    #             userGets.append(tempdict)
    #
    # if(order=='descend'):
    for k in range(len(myList)):
            tempdict = {
                'date': myList[len(myList)-k-1][0],
                'time': myList[len(myList)-k-1][1],
                'place': myList[len(myList)-k-1][2],
                'status': myList[len(myList)-k-1][3]
            }
            userGets.append(tempdict)

    return userGets

# x = getJSONData(awbNumber)
# pprint.pprint(x)
