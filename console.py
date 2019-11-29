# import ScrapeIntellicare

def header():
    print("Python Query Tool - ROW2")

    print("[1] Sample")
    print("[2] Sample")
    print("[3] Sample")
    print("[4] Sample")
    print("[5] Sample")
    print("[6] Sample")
    print("[7] Sample")
    print("[8] Sample")

def choice(inputValue):
    if (inputValue == '1'):
        #scrapeData
        saveFile()

    elif (inputValue == '2'):
        #scrapeData
        saveFile()

    elif (inputValue == '3'):
        #scrapeData
        saveFile()

    elif (inputValue == '4'):
        #scrapeData
        saveFile()

    elif (inputValue == '5'):
        #scrapeData
        saveFile()

    elif (inputValue == '6'):
        #scrapeData
        saveFile()

    elif (inputValue == '7'):
        #scrapeData
        saveFile()

    elif (inputValue == '8'):
        #scrapeData
        saveFile()

    else: 
        print("Incorrect choice!")

def saveFile():
    inputValue = input("Save File? (Y/N): ")

    if(inputValue == 'Y'):
        print("[1] Excell")
        print("[2] CSV")
        print("[3] TXT")

        choiceVal = input("choose a format: ")
        if (choiceVal == '1'):
            return choiceVal

        elif (choiceVal == '2'):
            return choiceVal

        elif (choiceVal == '3'):
            return choiceVal

        else:
            return '4'
            print("Incorrect choice!")


def main():
    header()
    inputValue = input("Enter your value: ")
    choice(inputValue)

if __name__ == '__main__':
    main()