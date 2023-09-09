import requests

def getRequest():
    url = 'https://dsa-ws01.umd.edu/DiningBusyMeter/get.json'
    response = requests.get(url, timeout=15)
    if response.status_code == 200:
        text = response.text
        charsToRemove = '[]{}"'
        for char in charsToRemove:
            text = text.replace(char, '')
        text = text[text.find(',')+1:]
        return text


def parse(info):
    statusList = ["\033[32mLess Busy", "\033[33mModerately Busy", "\033[31mExtremely Busy"]
    diningHalls = ["251 North", "South Campus", "Yahentamitsi"]
    split = info.split(',')
    hallIndex = 0
    for s in split:
        print(diningHalls[hallIndex] + "\t\t" + statusList[int(s[-1])-1] + "\033[37m")
        hallIndex += 1
def main():
    print("\033[1mHall\t\t\tStatus\n------------------------------------")
    parse(getRequest())
    print("\033[0m")


main()

