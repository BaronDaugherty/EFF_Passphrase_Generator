#@author: Baron Daugherty
#@date:   2017-05-10
#@desc:   Automates https://www.eff.org/dice
#@caveat: Download https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt first

#(pseudo) random numbers
import random

#runnin $h17
def main():
    #get a dictionary of codewords, make an empty list
    words = read()
    codes = []

    #add six codewords to the list
    for i in range(1,7):
        codes.append(words[roll()])

    #print the passphrase
    print(''.join(codes))

#read the words file, get a dictionary
def read():
    #dictionary
    d = {}
    #open the file... read only
    f = open('E:\Documents\Code\eff_large_wordlist.txt', 'r')
    #split each line into key:word and create the dictionary entries
    for line in f:
        x = line.split('\t')
        d[x[0]] = x[1].rstrip()
    #cleanliness is godliness... or so they say
    f.close()
    #return the dict
    return d

#ROLL OUT!    
def roll():
    #list of numbers
    r = []
    #seed for each roll
    random.seed()
    #get 5 numbers
    for i in range(1, 6):
        r.append(str(random.randint(1,6)))
    #return a 5 number string
    return ''.join(r)    

main()
