"""Generate a TAZ-based username for a fake twitter user."""
from numpy.random import choice

names = [
    "Justin",
    "Travis",
    "Griffin",
    "Clint",
    "McElroy",
    "Taako",
    "Magnus",
    "Merle",
    "Lup",
    "BarryBluejeans",
    "Lucretia",
    "Davenport",
    "Angus"
]
other = [
    "Fan",
    "Boi",
    "McElboy",
    "Lover",
    "Stan",
    "Goof"
]
number = [
    "1",
    "2",
    "3",
    "10",
    "69",
    "420",
    "5000",
    "9000"
]


def get_username():
    return(choice(names)+choice(other)+choice(number))
