import random
import pwinput
import string

# Welcome message printing function
def WelcomePrint(msg):
    length=len(msg)
    print()
    print("*"*length)
    print(msg)
    print("*"*length)

# hang man game function
def HangManGame():
    hangman_welcome="* WELCOME TO HANGMAN *"
    WelcomePrint(hangman_welcome)
    while(1):
        words=["Apple","Mango","Grape",
            "Pencil","Marker","Book",
            "Glass","Spoon","Plate",
            "Pumpkin","Potato","Carrot",
            "Cumin","Ajwain","Pepper",
            "Soap","Shampoo","Bucket",
            "Trolley","HandBag","SlimBag",
            "Virat","Surya","Sachin",
            "Hockey","Cricket","Tennis",
            "Titanic","KGF","Bahubali"]
        ind=random.randint(1,30)
        # print("ind : ",ind,"words[ind] : ",words[ind])
        print("Guess the word! Hint: Word is a",end=" ")
        if(ind<3):
            print("fruit")
        elif(ind<6):
            print("part of drawing kit")
        elif(ind<9):
            print("utensils")
        elif(ind<12):
            print("Vegetable")
        elif(ind<15):
            print("part of Spices")
        elif(ind<18):
            print("Part of bathroom kit")
        elif(ind<21):
            print("part of travel accessories")
        elif(ind<24):
            print("Cricketer name")
        elif(ind<27):
            print("Game")
        elif(ind<30):
            print("Movie name")

        temp=list(words[ind].lower())
        temp1=list(words[ind].lower())
        length=len(temp)
        print(" _"*length)
        print(f"\nYOU HAVE {length+2} CHANCES\n")
        guess_word=list("_"*length)
        success=0
        for i in range(length+2):
            val=input("Enter a letter to guess: ").lower()
            if val in temp:
                a=temp.index(val)
                guess_word.pop(a)
                guess_word.insert(a,val)
                temp[a]=0
                
            for j in guess_word:
                print(j,end=" ")
                if(guess_word == temp1):
                    print(f"\nCongratulations! You guessed the word {words[ind]}\n")
                    success=1
                    break
            if(success==1):
                break
            print()
        if "_" in guess_word:
            print(f'\nTry Again! The word is {words[ind]}\n')
        print("Would you like to play again?\n" \
        "Press 1 for yes\n" \
        "Press 0 for Exit\n")
        response=input("PLEASE ENTER YOUR INPUT: ")
        if(response=='0'):
            break

# COWS AND BULLS GAME FUNCTION
def CowsAndBullsGame():
    cowsandbulls_welcome="* WELCOME TO COWS AND BULLS *"
    WelcomePrint(cowsandbulls_welcome)

    n=int(input("\nPLEASE ENTER NUMBER OF PLAYERS: "))
    no_of_tries=[0 for i in range(n)]
    secret_codes=[]
    print(f'SECRET CODE IS 4-DIGIT AND WITHOUT DUBLICATE')
    if(n>1):
        for i in range(1,n+1):
            while(1):
                while(1):
                    print(f'Player{i}:')
                    # val=(input("ENTER YOUR SECRET CODE: "))
                    val=pwinput.pwinput(prompt="ENTER YOUR 4-DIGIT SECRET CODE: ",mask="*")
                    if(len(val)==4):
                        break
                val_list=list(val)
                length=len(val_list)
                for j in range(length):
                    a=val_list.count(val_list[j])
                    if(a>1):
                        print("DIGITS SHOULD NOT BE REPEATED")
                        break
                if(j==(length-1)):
                    break    
            secret_codes.append(val)
    else:
        digits=string.digits
        val=(random.sample(digits,4))
        val="".join(val)
        secret_codes.append(val)

    for i in range(1,n+1):
        while(1):
            temp=i+1-((i==n)*(n))
            while(1):
                print(f"\nPLAYER{i} PLEASE GUESS THE SECRET CODE OF PLAYER{temp}\n")
                guess=input("PLEASE ENTER YOUR 4-DIGIT INPUT: ")
                if(len(guess)==4):
                    break

            guess_list=list(guess)
            expected=secret_codes[temp-1]
            expected_list=list(expected)
            no_of_tries[i-1]+=1
            bull_count=0
            cow_count=0
            for j in range(4):
                if(guess_list[j]==expected_list[j]):
                    bull_count+=1
                elif(guess_list[j] in expected_list):
                    cow_count+=1
            print("\nbull_count:",bull_count,"cow_count:",cow_count)
            if(bull_count==4):
                print(f"\n\nCONGRATULATIONS PLAYER{i}! YOU GUESSED IT RIGHT IN {no_of_tries[i-1]} changes!\n")
                break
    min_val=min(no_of_tries)
    count_val=no_of_tries.count(min_val)
    if(count_val==1):
        print(f"\n\nWINNER OF THE GAME IS PLAYER{(no_of_tries.index(min_val))+1}\n")
    else:
        print("\n\nGAME IS DRAW...!\n")

def QuizGame():
    quiz_welcome="* WELCOME TO QUIZ *"
    WelcomePrint(quiz_welcome)

    print("\n\nYOU HAVE 10 QUESTIONS TO ANSWER\n\n" \
    "PRESS 1 TO START THE QUIZ\n" \
    "PRESS 0 TO EXIT\n")
    status = int(input("PLEASE ENTER YOUR INPUT:"))
    if(status):
        print("\n1. WHICH PLANET IS KNOWN AS 'RED PLANET'?")
        ans=input("Answer: ").lower()
        if(ans=="mars"):
            print("\nYOU ANSWERED IT RIGHT...!\n\n" \
            "YOUR NEXT QUESTION:")
        else:
            print("\nWRONG ANSWER\n\n" \
            "YOUR NEXT QUESTION:")
        
        print("2. WHAT HAS A FACE AND TWO HANDS, BUT NO ARMS OR LEGS?")
        ans=input("Answer: ").lower()
        if(ans=="clock"):
            print("\nYOU ANSWERED IT RIGHT...!\n\n" \
            "YOUR NEXT QUESTION:")
        else:
            print("\nWRONG ANSWER\n\n" \
            "YOUR NEXT QUESTION:")
                
        print("3. WHAT IS THE CURRENCY OF JAPAN?")
        ans=input("Answer: ").lower()
        if(ans=="japanese yen"):
            print("\nYOU ANSWERED IT RIGHT...!\n\n" \
            "YOUR NEXT QUESTION:")
        else:
            print("\nWRONG ANSWER\n\n" \
            "YOUR NEXT QUESTION:")
        
        print("4. WHAT IS MOST WIDELY SPOKEN LANGUAGE IN THE WORLD?")
        ans=input("Answer: ").lower()
        if(ans=="mandarin chinese"):
            print("\nYOU ANSWERED IT RIGHT...!\n\n" \
            "YOUR NEXT QUESTION:")
        else:
            print("\nWRONG ANSWER\n\n" \
            "YOUR NEXT QUESTION:")
        
        print("5. WHAT COMES ONCE IN A MINUTE, TWICE IN A MOMENT BUT NEVER IN THOUSAND YEARS?")
        ans=input("Answer: ").lower()
        if(ans=="m"):
            print("\nYOU ANSWERED IT RIGHT...!\n\n" \
            "THANK YOU FOR PARTICIPATING...! HOPE YOU ENJOYED THE QUIZ\n")
        else:
            print("\nWRONG ANSWER\n\n" \
            "THANK YOU FOR PARTICIPATING...! HOPE YOU ENJOYED THE QUIZ\n")
        
# main code
try:
    welcome_msg="* WELCOME TO GAMEZONE *"
    WelcomePrint(welcome_msg)
    while(1):
        print("GAMEZONE CONTAINS:\n1. HANG MAN\n2. COWS AND BULLS\n3. QUIZ")
        print("\nPRESS 1 FOR 'HANG MAN'" \
        "\nPRESS 2 FOR 'COWS AND BULLS'" \
        "\nPRESS 3 FOR 'QUIZ'\n")

        GAME=int(input("PLEASE ENTER YOUR INPUT: "))

        if (GAME == 1):
            HangManGame()
        elif(GAME == 2):
            CowsAndBullsGame()
        elif(GAME == 3):
            QuizGame()
        else:
            print("\nINVALID INPUT...!!!\n")
        print("\nWOULD YOU LIKE TO PLAY OTHER GAMES?\n" \
            "PRESS 1 FOR YES\n" \
            "PRESS 0 FOR NO\n")
        status=int(input("PLEASE ENTER YOUR INPUT: "))
        if(status==0):
            break;
        elif(status==1):
            continue;
except KeyboardInterrupt:
    print("\n\nGAME IS INTERRUPTED! EXITING...\n\n")
    exit()
              