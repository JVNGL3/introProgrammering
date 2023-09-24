#!/usr/bin/python3

antal = 0




for i in range(10):
    antal += 1
    if (antal%4) == 0:
        pan = antal/4
    else:
        pan = (antal - (antal%4))/4  + 1
    print("antal", antal)
    print("pans:", pan)
    print("----------------")