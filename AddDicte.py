import json
file = './data.json'
import os
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getInfo(file):
    objNum = 0
    titles = []
    texts = []
    with open(file, 'r') as f:
        data = json.load(f)
        for i in data:
            objNum +=1
        for i in range(objNum):
            title = data[f"{i}"]["title"]
            titles.append(title)
        for i in range(objNum):
            text = data[f"{i}"]["text"]
            texts.append(text)
        f.close()
    return [ titles, texts ]

# with open('./data.json', 'w') as f:
#     a = json.dumps(data, indent=4)
#     json.dump(data, f)
#     f.close()

def main():
    os.system('clear')
    option = input("Do you want to add or delete entry?[add/del]: ")
    if option == 'add' or option == 'del':
        if option == "del":
            data = getInfo(file)
            titles = data[0]
            for i in range(len(titles)):
                print(f"{i+1}) {titles[i]}")    
            entryNum = input("Which entry do u want to delete? : ")
            
            with open('./data.json', 'r') as f:
                data = json.load(f)
                f.close()

            with open('./data.json', 'w') as f:
                del data[f"{int(entryNum) - 1}"]
                oldEntry = 0
                for entry in list(data):
                    if int(entry) != oldEntry:
                        data[f"{oldEntry}"] = data.pop(entry)
                    else:
                        pass
                    oldEntry +=1
                f.seek(0)
                f.write(json.dumps(data, indent=4))
                f.close()
                print(f"{bcolors.OKGREEN}DONE!")

        elif option == 'add':
            with open('./data.json', 'r+') as f:
                data = json.load(f)
                title = input("Title: ")
                text = input("Text(make sure it's one paragraph): ")
                newLine = len(data)
                data[f"{newLine}"] = {"title": title, "text": text}
                jsonDump = json.dumps(data, indent=4)
                f.seek(0)
                f.write(jsonDump)
                f.close()
                print(f"{bcolors.OKGREEN}DONE!")
                
        pass


    
       

main()
