#!/usr/bin/python3

"""
Codewars: A Wolf in Sheep's Clothing

Wolves have been reintroduced to Great Britain.
You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten.
Remember that you are standing at the front of the queue which is at the end of the array:

"""


def warn_the_sheep(queue):
    for i in queue:
        try:
            if i == "wolf":
                wolfInd = queue.index(i)
                if queue[wolfInd +1] == "sheep":
                    sheepNum = len(queue)-(wolfInd+1)
                    return f"Oi! Sheep number {sheepNum}! You are about to be eaten by a wolf!"
        except IndexError:
            return "Pls go away and stop eating my sheep"






