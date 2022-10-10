# Sorting a list by the second element on the sublist
# using Bubble-sort method

def sort_list(sList):

    length = len(sList)

    for i in range(0, length):
        for j in range(0, length - i - 1):
            if sList[j][1] > sList[j + 1][1]:

                sList[j][1], sList[j + 1][1] = sList[j + 1][1], sList[j][1]

    return sList

sList = [['Mike', 32], ['Phiona', 30], ['Henry', 28], ['Charles', 23], ['Kilian', 22], ['Kevin', 19]]
print(sort_list(sList))


