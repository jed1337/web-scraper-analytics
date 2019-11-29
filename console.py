import MusicDataExtraction as mde
import Questions as q
import writer as w

def header():
    print("***** Python Query Tool *****")
    print("\n")

    print("[1] Which artists&songs have been included in Top 10 from 2014-2018 every 25 December?\n")
    print("[2] Which artist&song have the highest points from 2014 - 2018 every 25th of December?\n")
    print("[3] From 2014 - 2018 every 25th of December, what are the accumulated total points of Top 10 songs/singers?\n")
    print("[4] What are the Top 10 artists&songs that were recognized by top countries of music industry (US, UK, DE, AU, JP)?\n")
    print("[5] Which songs&singers belong to the lowest 10 from 2014 - 2018 25th of December?\n")
    print("[6] From 2014 - 2018 25th of December, how many times did Mariah Carey belonged to Top 5?\n")
    print("[7] Which artist&song have the lowest points from 2014 - 2018 every 25th of December?\n")
    print("[8] From 2014 - 2018 25th of December, what artists&songs garnered the highest total points(TPTs) per year?\n")
    
def choice(inputValue):
    if (inputValue == '1'):
        q1 = q.Question1(mde.extract())
        q1.quickAnswer()
        saveFile(q1.outputdata())
        
    elif (inputValue == '2'):
        q2 = q.Question2(mde.extract())
        q2.quickAnswer()
        saveFile(q2.outputdata())

    elif (inputValue == '3'):
        q3 = q.Question3(mde.extract())
        q3.quickAnswer()
        saveFile(q3.outputdata())

    elif (inputValue == '4'):
        q4 = q.Question4(mde.extract())
        q4.quickAnswer()
        saveFile(q4.outputdata())

    elif (inputValue == '5'):
        q5 = q.Question5(mde.extract())
        q5.quickAnswer()
        saveFile(q5.outputdata())

    elif (inputValue == '6'):
        q6 = q.Question6(mde.extract())
        q6.quickAnswer()
        saveFile(q6.outputdata())

    elif (inputValue == '7'):
        q7 = q.Question7(mde.extract())
        q7.quickAnswer()
        saveFile(q7.outputdata())

    elif (inputValue == '8'):
        q8 = q.Question8(mde.extract())
        q8.quickAnswer()
        saveFile(q8.outputdata())

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