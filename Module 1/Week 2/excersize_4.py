import numpy as np


def levenshtein(source,target):
    # print(source)
    # print(target)
    matrix = np.zeros((len(source) , len(target) ))
    for i in range(len(source)):
        for j in range(len(target)):
            matrix[i][j] = 1000000
    matrix[0][0] = 0
    for i in range(len(source) ):
        for j in range(len(target)):
            if i-1>=0:
                matrix[i][j] = min(matrix[i][j],matrix[i-1][j] + 1)
            if j-1>=0:
                matrix[i][j] = min(matrix[i][j],matrix[i][j-1] + 1)
            if i-1>=0  and j-1>=0:
                matrix[i][j] = min(matrix[i][j], matrix[i-1][j-1]+ (source[i]!= target[j]))
    # return matrix[len(source)][len(target)]
    # print(matrix)
    return matrix[len(source)-1][len(target)-1]
source = input()
target = input()

source = '#' + source
target = '#' + target

# levenshtein(source,target)
print(levenshtein(source,target))



        