#!/usr/bin/python3

def recept(antal):
    #used for calculating the right amounts
    eq = antal/4
    
    #in grams
    butterToCake = eq * 75 
    
    #in whole eggs
    eggsToCake = round(eq * 3)

    #in decilitres
    sugarFlour = eq * 3

    #in teaspoons
    bakingVanilla = eq * 2

    #in decilitres
    waterToCake = eq * 1

    if (antal%4) == 0:
        pan = eq
    else:
        pan = (antal - (antal%4))/4  + 1
    #in grams
    butterToPan = pan * 15
    #in tablespoons
    breadcrumbsToPan = pan * 3

    #prints the ingredients to the terminal
    print("För formen:\nca", butterToPan, "g smör\nca", breadcrumbsToPan, "msk ströbröd")
    print("\nFör kakan:")
    print("",eggsToCake, "st ägg\n",sugarFlour, "dl strösocker\n",bakingVanilla, "tsk vaniljsocker\n",bakingVanilla, "tsk bakpulver\n",sugarFlour, "dl vetemjöl\n",butterToCake, "g smör\n",waterToCake, "dl vatten\n")

def tidblanda(antal):
    #10 minute standard time plus 1 minute for every person
    return 10 + antal

def tidgradda(antal):
    #30 minute standard time plus 3 minutes for ever person
    return 30 + 3*antal


def sockerkaka(antal):
    print("Ett recept för ",antal," personer\n")
    recept(antal)
    tid = tidblanda(antal) + tidgradda(antal)
    print("Detta är beräknat att ta: ",tid, "minuter")
          

sockerkaka(4)
print("----------------------------------------")
sockerkaka(7)