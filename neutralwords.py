import re as re
def settingupfile():
    f = open("Inferno.txt", 'r') #opens dataset
    f = f.read() #reads dataset
    print(re.findall(r"([^.]*?Luca[^.]*\.)", f)) #prints all sentences that contain Luca. Sentences are then copied and pasted into a text file.


def neutralwords():
    file = open("lucamafiosa.txt", "r") #text file containing sentences
    file = file.read() #reads file
    neutral = ('disinterested ordinary fair-minded inactive indifferent nonaligned nonpartisan unbiased uncommitted undecided uninvolved calm cool noncombatant aloof bystanding clinical collected detached disengaged dispassionate easy impersonal inert middle-of-road nonbelligerent nonchalant nonparticipating sidelines fence pacifistic poker-faced relaxed unaligned unconcerned unprejudiced fair vague abstract achromatic drab intermediate vanilla colorless expressionless indeterminate indistinct indistinguishable toneless undefined outside aloof candid casual dispassionate equitable impartial impersonal incurious composed cool quiet serene temperate unexcitable unexcited just moderate neutral non-discriminatory balanced bearable cautious conservative gentle limited peaceable tranquil untroubled deliberate disciplined even measured midway nonpartisan pacific reserved pleasant reasonable soft steady tame tolerable tolerant abstinent compromising considered mild bearable average')
    # a list of a hundred neutral words
    checkneutral = any(item in file for item in neutral) #checks if any of the neutral words occur in sentences gathered.
    # checkneutral returns True or False
    if checkneutral is True:
        print("Contains neutral words.")
    else:
        print("No neutral words.")
    wordcount =[] #blank list
    neutralwordcount = sum(file.count(x) for x in neutral.split()) #calculates all the matches of neutral words
    print(neutralwordcount) #displays the sum of neutal words
    wordcount.append(neutralwordcount) #adds this number to list

    print(file.count('laugh'))


settingupfile()
neutralwords()