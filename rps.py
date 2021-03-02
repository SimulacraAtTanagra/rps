# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 23:12:58 2020

@author: shane
"""
import random
#simple rock papers scissors game for S&G

def gameround():
    selections=['rock','paper','scissors']
    playdict={ix+1:i for ix,i in enumerate(selections)}
    selections.extend(selections)
    windict={}
    try:
        [windict.update({i+selections[ix-1]:'win'}) for ix,i in enumerate(selections)]
        [windict.update({i+selections[ix]:'draw'}) for ix,i in enumerate(selections)]
        [windict.update({i+selections[ix+1]:'lose'}) for ix,i in enumerate(selections)]
    except:
        pass
    print("Beginning of round")
    bot=me=0
    while True:
        guess=int(input("\nInput 1, 2 or 3. 1 for Rock, 2 for Paper and 3 for scissors\nI choose...:"))
        botguess=random.randint(1,3)
        print(f'You picked {playdict[guess]} and the computer picked {playdict[botguess]}\n')
        x=windict[selections[guess]+selections[botguess]]
        print(f'\nYou {x}!\n')
        me+=int(x=="win")
        bot+=int(x=="lose")
        print(f'\nCurrent count is \n You: {me} \n Computer: {bot}')
        if bot ==3 or me == 3:
            print("\nBeen nice playing with you, partner")
            break   
        