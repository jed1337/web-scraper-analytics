import ExtractMusicData as em
import writer as w

def header():
    print("Python Query Tool")

    print("Which artists&songs have been included in Top 10 from 2014-2018 every 25 December?")
    print("Which artist&song have the highest points from 2014 - 2018 every 25th of December?")
    print("From 2014 - 2018 every 25th of December, what are the accumulated total points of Top 10 songs/singers?")
    print("What are the Top 10 artists&songs that were recognized by top countries of music industry (US, UK, DE, AU, JP)?")
    print("Which songs&singers belong to the lowest 10 from 2014 - 2018 25th of December?")
    print("From 2014 - 2018 25th of December, how many times have Mariah Carey belonged to Top 5?")
    print("[7] Sample")
    print("[8] Sample")

def choice(inputValue):
    if (inputValue == '1'):
        em.question1.quickAnswer()
        saveFile(em.question1.outputdata())

    elif (inputValue == '2'):
        em.question2.quickAnswer()
        saveFile(em.question2.outputdata())

    elif (inputValue == '3'):
        em.question3.quickAnswer()
        saveFile(em.question3.outputdata())

    elif (inputValue == '4'):
        em.question4.quickAnswer()
        saveFile(em.question4.outputdata())

    elif (inputValue == '5'):
        em.question5.quickAnswer()
        saveFile(em.question5.outputdata())

    elif (inputValue == '6'):
        em.question6.quickAnswer()
        saveFile(em.question6.outputdata())

    elif (inputValue == '7'):
        em.question7.quickAnswer()
        saveFile(em.question7.outputdata())

    elif (inputValue == '8'):
        em.question8.quickAnswer()
        saveFile(em.question8.outputdata())

    else: 
        print("Incorrect choice!")

def saveFile(rawData):
    inputValue = input("Save File? (Y/N): ")

    if(inputValue == 'Y'):
        print("[1] Excel")
        print("[2] CSV")
        print("[3] TXT")

        choiceVal = input("Choose a format: ")
        if (choiceVal == '1'):
            return w.excel_writer(rawData)

        elif (choiceVal == '2'):
            return w.csv_writer(rawData)

        elif (choiceVal == '3'):
            return w.txt_writer(rawData)

        else:
            print("Incorrect choice!")


def main():
    header()
    inputValue = input("Enter your value: ")
    choice(inputValue)

if __name__ == '__main__':
    main()