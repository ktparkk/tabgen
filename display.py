from math import trunc
from random import randint, choice
from nodes import Node, genNodes

def dispNodes(lst, melody):
    table = ""
    for level, pitch in zip(lst, melody):
        table += pitch + ": "
        for node in level[0:len(level)-2]:
            table += str(node.fret) + "(" + node.string + ") "
        table += "\n"
    return table


def dispTab(lst,instrument): # displays ASCII tablature
    lines = []
    for i in instrument:
        lines.append(i[0]+"|")
    i = 0
    for i in lst:
        j = 0
        for j in lines:
            dashnum = len(str(i[0])) + 1
            if j == i[1]:
                #to do: fill it bitch
                lines[j] += str(i[0])
                lines[j] += "-"
            else:
                lines[j] += "-" * dashnum
            j += 1
        i += 1
    lines.reverse()
    return lines
