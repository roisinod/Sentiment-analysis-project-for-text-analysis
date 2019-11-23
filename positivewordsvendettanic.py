import re as re
def settingupfile():
    f = open("Vendetta.txt", 'r') #opens dataset
    f = f.read() #reads dataset
    print(re.findall(r"([^.]*?Nic[^.]*\.)", f)) #prints all sentences that contain Nic. Sentences are then copied and pasted into a text file


def positivewords():
    file = open("happy.txt.txt", "r") #text file containing sentences
    file = file.read() #reads file
    positive = ('constructive effective forward-looking good practical productive reasonable useful affirmative progressive sound efficacious cheerful contented delighted ecstatic elated glad joyful joyous jubilant lively laugh merry overjoyed peaceful pleasant pleased thrilled upbeat blessed blest blissful blithe captivated chipper chirpy content convivial exultant flying high gay gleeful gratified intoxicated jolly laughing light looking-good mirthful peppy perky playful sparkling sunny tickled up embrace feel kiss caress clasp cling cosset court cuddle fondle hold hug lick neck pet press shine soothe stroke tryst love happy hopeful hope affable courteous courtly genial ingratiating polite soft-spoken sophisticated urbane worldly agreeable bland civilized cordial cute handsome chuckle smile')
    # a list of a hundred positive words
    check_positive = any(item in file for item in positive) #checks if any of the positive words occur in sentences gathered.
    # check_positive returns True or False
    if check_positive is True:
        print("Contains positive words.")
    else:
        print("No positive words.")
    wordcount =[] #blank list
    positive_word_count = sum(file.count(x) for x in positive.split()) #calculates all the matches of positive words
    print(positive_word_count) #displays the sum of positive words
    wordcount.append(positive_word_count)  #adds this number to list

    print(file.count('laugh'))



settingupfile()
positivewords()