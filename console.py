import question1 as q1
import question2 as q2
import question5 as q5
import question6 as q6
import question7 as q7
import question8 as q8
import writer as w

def header():
    print("***** Python Query Tool *****")
    print("\n")

    print("[1] Which artists&songs have been included in Top 5 from 2014-2018 every 25 December?\n")
    print("[2] Which artist&song have the highest points from 2014 - 2018 every 25th of December?\n")
    print("[3] From 2014 - 2018 every 25th of December, what are the accumulated total points of Top 10 songs/singers?\n")
    print("[4] What are the Top 10 artists&songs that were recognized by top countries of music industry (US, UK, DE, AU, JP)?\n")
    print("[5] Which songs&singers belong to the lowest 10 from 2014 - 2018 25th of December?\n")
    print("[6] From 2014 - 2018 25th of December, how many times did Mariah Carey belonged to Top 5?\n")
    print("[7] Which artist&song have the lowest points from 2014 - 2018 every 25th of December?\n")
    print("[8] From 2014 - 2018 25th of December, what artists&songs garnered the highest total points(TPTs) per year?\n")
    
def choice(inputValue):
    if (inputValue == '1'):
        q1.question1()
        
    elif (inputValue == '2'):
        q2.question2()

    elif (inputValue == '3'):
        print('Not implemented')

    elif (inputValue == '4'):
        print('Not implemented')

    elif (inputValue == '5'):
        q5.question5()

    elif (inputValue == '6'):
        q6.question6()

    elif (inputValue == '7'):
        q7.question7()

    elif (inputValue == '8'):
        q8.question8()

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
