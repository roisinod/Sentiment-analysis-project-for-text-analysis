import re as re
def settingupfile():
    f = open("mafiosa.txt", 'r') #opens dataset
    f = f.read()#reads dataset
    print(re.findall(r"([^.]*?Luca[^.]*\.)", f)) #prints all sentences that contain Luca. Sentences are then copied and pasted into a text file

def negwords():
    file = open("lucamafiosa.txt", "r") #text file containing sentences
    file = file.read()#reads file
    negative = ('adverse gloomy pessimistic unfavourable weak abrogating annulling anti con contrary contravening denying disallowing opposing recusant refusing rejecting removed resisting against antagonistic balky colorless counteractive cynical detrimental dissentient nugatory privative repugnant resistive unaffirmative unenthusiastic uninterested unwilling bleak cloudy dim dismal dreary dull murky reluctant stuffy unfriendly unlucky bad hate negative unwilling down glare glower grimace pout gloom lower sulk glower grimace scowl sick criminal assassin mafia evil violent violence angry annoyed fight hissed snapped enemy murder assault attack fighting cruel storm impatience exasperation fury temper rage outrage irritability irritation mad hatred punch kick force push dislike disapproval disgust offense distaste reluctance')
    #a list of a hundred negative words
    checkneg = any(item in file for item in negative) #checks if any of the negative words occur in sentences gathered.
    #checkneg returns True or False
    if checkneg is True:
        print("Contains negative words.")
    else:
        print("No negative words.")
    wordcount =[] #blank list
    negwordcount = sum(file.count(x) for x in negative.split()) #calculates all the matches of negative words
    print(negwordcount) #displays the sum of negative words
    wordcount.append(negwordcount) #adds this number to list

    print(file.count('laugh')) #can look for individual words in sentences with Nic or Luca


settingupfile()
negwords()