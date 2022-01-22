from enum import Enum


class Day(Enum):
    January = 1
    February = 2
    March = 3


# print the enum member
print(Day.March)

# get the name of the enum member
print(Day.February.name)

# get the value of the enum member
print(Day.January.value)
