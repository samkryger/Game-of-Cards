from dealer import Dealer
dealer1 = Dealer()

def menu():
    dealerChoice = input(f'''
                (1). Shuffle
                (2). Deal a Card
                (3). Recycle Dealt Cards
                Enter Choice: ''')
    if(dealerChoice == '1'):
        dealer1.shuffle()
        print("Shuffled")
    elif(dealerChoice == '2'):
        choice = 'Y'
        while(choice == 'Y' or choice == 'y'):
            dealer1.deal()
            choice = str(input("Another?(Y or N) "))
    elif(dealerChoice == '3'):
        dealer1.recycle()
        print("Cards Returned + Shuffled")
        
backtomenu = 'Y'
while(backtomenu == 'Y' or backtomenu == 'y'):
    menu()
    backtomenu = str(input("Back to Menu?(Y or N) "))
