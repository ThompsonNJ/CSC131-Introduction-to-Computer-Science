#==========================================================================
# PROGRAM PURPOSE:... C9 Translator
# AUTHOR:............ Thompson, Nick
# COURSE:............ CSC 131-004
# TERM:.............. Fall 2017
# COLLABORATION:.....                       
# WORK TIME(h:mm):... 4:00
#==========================================================================
'''The purpose of this program is to allow users to input Spanish and/or French
translations for English words or phrases to a text document. The user can search
for the translated word or see all translated words using the menu.'''

# functions
def mainmenu():
    '''This function is the menu for the program. It returns the menu
selection as x.'''
    
    print("Main Menu")
    print("1 - translate a word")
    print("2 - add a word to the dictionary")
    print("3 - print current translation dictionary")
    print("4 - exit")
    print("==========================================================================")
    
    while True:
        try:
            x = int(input("Please make a selection: "))
            if x in range(1,5):
                return x
            
            else:
                print("**Invalid Entry!")
        except:
            print("**Invalid Entry!")

# init
file = open("translation.txt", 'r+')
aname = file.read().splitlines()
langDic = {}

print("The purpose of this program is to allow users to input Spanish and/or French\n\
translations for English words or phrases to a text document. The user can\n\
search for the translated word or see all translated words using the menu.")
print()
print("If the word you want translate is more than one word,\n\
use '_' instead of using a space. (ex: por_favor)")
print()

for i in range(len(aname)):
    aname[i] = aname[i].split(' ')

for line in aname:
    langDic[line[0]] = {"Spanish": line[1], "French": line[2]}
    
# start        
while True:    
    x = mainmenu()
    
    if x == 1:
        ui = input("Please enter a word in English: ")
        
        if ui not in langDic:
            print("Sorry! No translation '{}' yet.".format(ui))
            
            while True:
                try:
                    isin = input("Would you like to add it? y/n: ")
                    
                    if isin == 'y':
                        break
                    elif isin == 'n':
                        break
                    else:
                        raise ValueError
                    
                except:
                    ValueError
                    print("**Invalid Entry!")
            
            if isin == 'y':                
                while True:
                    try:
                        addspantran = input("Please input the Spanish translation for '{}': ".format(ui))
                        addfrenchtran = input("Please input the French translation for '{}': ".format(ui))
                        break
                        
                    except:
                        print("Invalid Entry!")
   
                langDic[ui] = {'Spanish': addspantran, 'French': addfrenchtran}

                if len(aname) == 0:
                    newline = ("{0} {1} {2}".format(ui, addspantran, addfrenchtran))
                    
                else:
                    newline = ("\n{0} {1} {2}".format(ui, addspantran, addfrenchtran))
                    
                file.write(newline)
                print(langDic[ui])
                print()
                
            elif isin == "n":
                 print()
                
        else:
            print(langDic[ui])

    if x == 2:
        addengword = input("What English word are you providing a translation for: ")
        addspantran = input("Please input the Spanish translation for '{}': ".format(addengword))
        addfrenchtran = input("Please input the French translation for '{}': ".format(addengword))

        langDic[addengword] = {'Spanish': addspantran, 'French': addfrenchtran}
        
        if len(aname) == 0:
            newline = ("{0} {1} {2}".format(addengword, addspantran, addfrenchtran))
                    
        else:
            newline = ("\n{0} {1} {2}".format(addengword, addspantran, addfrenchtran))
            
        file.write(newline)        
        print(langDic[addengword])
        print()
        
    if x == 3:
        print()
        print(langDic)
        print()

    if x == 4:
        print("Goodbye!")
        file.close()
        break
