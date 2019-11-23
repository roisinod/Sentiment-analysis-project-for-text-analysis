import re
f = open("Vendetta.txt", 'r') #opens dataset
f = f.read() #reads dataset
print(f)
v = f.translate({ord(i): None for i in '?.'',(0):;!"'}) #cleans dataset
#print(v)
check = re.findall(r'Nic', v) #Finds all occurrences of Nic
print(check) #prints every mention of Nic in dataset
count =[] #blank list
count.append(v.count('Nic')) #sums the number of Nics in check
print('The count of Nic is:', count) #displays the count
neg = []
pos = []
if len(count) >= 1:
    print('yay')
    pos.extend(count)
else:
    print('hello')
    neg.extend(count)
print('positive', (pos))
print('neg', (neg))
print('----')
check2 = re.findall(r'Luca', v)
print(check2)
count2 =[]
count2.append(v.count('Luca'))
print('The count of Luca is:', count2)
neg2 = []
pos2 = []
if len(count2) >= 1:
    print('yay')
    pos2.extend(count2)
else:
    print('hello')
    neg2.extend(count2)
print('positive', (pos2))
print('neg', (neg2))
