##2021041035 조민규##


import operator

trainTupleList = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5), ('토마스', 4), ('헨리', 7),
                  ('토마스', 3), ('에밀리', 8), ('퍼시', 5), ('고든', 13)]
trainDic, trainList = {}, []
tempTup = None
totalRank, currentRank = 1, 1

if __name__ == "__main__":
    for tempTup in trainTupleList:
        tName = tempTup[0]
        tWeight = tempTup[1]
        if tName in trainDic:
            trainDic[tName] += tWeight
        else:
            trainDic[tName] = tWeight

    print('기차 수송량 목록 ==> ', trainTupleList)
    print('-----------------------------------')
    trainList = sorted(trainDic.items(), key = operator.itemgetter(1), reverse = True)

    print('기차   총 수송량   순위')
    print('-----------------------------------')
    print(trainList[0][0], '\t', trainList[0][1], '\t', currentRank)

    for i in range(1, len(trainList)):
        totalRank += 1
        if trainList[i][1] == trainList[i-1][1]:
            pass
        else:
            currentRank = totalRank
        print(trainList[i][0], '\t', trainList[i][1], '\t', currentRank)
