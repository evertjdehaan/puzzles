# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:13:06 2016

@author: evehaa
"""

from getwords import getwords

allwords = getwords(minlen=4, maxlen=11)

greens = []
green_vals = [2, 5, 8, 11, 14, 17, 20, 23, 26]
for i1 in green_vals:
    for i2 in green_vals:
        for i3 in green_vals:
            for i4 in green_vals:
                if (i1+i2+i3+i4) == 62:
                    greens.append("{}{}{}{}".format(
                        chr(i1+64), chr(i2+64), chr(i3+64), chr(i4+64)))
                            
blues = []
blue_vals = [3, 6, 9, 12, 15, 18, 21, 24]
for i1 in blue_vals:
    for i2 in blue_vals:
            if (i1+i2) == 27:
                blues.append("{}{}".format(
                    chr(i1+64), chr(i2+64)))
            
print(len(greens)*len(blues))
i = 0
j = 0                
with open('AIVD17b2.txt', 'w') as f:
    for green in greens:
        j += 1
        for blue in blues:
            permutation = ('hoeov'+green[0]+blue[0]+green[1]+blue[1]
                            +green[2:4]).lower()

            if (i % 1000) == 0:
                print('{:.2f}\t{}'.format(j/len(greens), permutation))
            i += 1

            for w in allwords:
                if w in permutation:
                    f.write(w + '\t\t' + permutation + '\r\n')
