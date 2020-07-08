from random import *

def englishDict(): #reading the text file to a list
    s=open("englishWords.txt","r",encoding="utf-8")
    dictionary=s.read().split()
    s.close()
    return dictionary

def word_selection(dict):  #selecting random word from the list dictionary
    num=randint(0,len(dict))
    return dict[num]

def list_to_str(lst):  #makes a list of elements a string
    s=''
    for x in range(len(lst)):
        s+=lst[x]

    return s

def check(word,char,dis): #checks if char exits in word and modifies dis if so
    lst=[]
    for i in range(len(word)):
        if(word[i]==char):
            lst.append(i)

    if(len(lst)==0):
        return 0
    else:
        return add_display(dis,lst,char)

def add_display(dis,lst,char):
    dis=list(dis)
    for i in range(len(lst)):
        dis[lst[i]]=char

    dis=list_to_str(dis)

    return dis

def print_list(used): #prints used letters 
    s=''
    for x in range(len(used)):
        s+="{},".format(used[x])
    print("Used letters:{}\n".format(s))

def check_in_alphabet(char): #checks if char is not in the english alphabet 
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if(len(char)==1 and char in alphabet):
        return 1
    else:
        return 0

def play(word_bot):  #main function that lets you play the game
    lives=7
    dis=" "
    used=[]
    print("Length of word:{}\n".format(len(word_bot)))
    for i in range(len(word_bot)-1):
        dis+=' '
    while(lives!=0):
        print("Lives:{}".format(lives))
        print_list(used)
        char=input("Guess letter:\n")
        if(check_in_alphabet(char)):
            if(char not in used):
                if(check(word_bot, char, dis) == 0):
                    print("No {} in the hangman's word".format(char))
                    used.append(char)
                    print("Word |{}|".format(dis))
                    lives = lives - 1
                else:
                    dis = check(word_bot, char, dis)
                    print("Found a letter!")
                    print("Word: |{}|".format(dis))
                    used.append(char)

                if (dis == word_bot and lives != 0):
                    print("End of game word is |{}|".format(dis))
                    break
                elif (lives == 0):
                    print("\nHangman died. Word was:{}".format(word_bot))
                    break
                else:
                    continue
            else:
                print("You have used {} again".format(char))
                print("Word:|{}|".format(dis))
                continue
        else:
            print("Letter not string or number. Spaces not allowed")
            continue


dict=englishDict()
word=word_selection(dict)
play(word)
