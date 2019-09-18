def invertedIndex(docList):
    pairSet = set()
    docNumber = 1
    for doc in docList:
        for word in doc.split():
            pairSet.add((word, docNumber))
        docNumber = docNumber + 1

    # pairList = sorted(sorted(pairSet, key=lambda x: x[1]), key=lambda x: x[0])
    # print(pairList)

    invertedIndex = {}
    for pair in pairSet:
        if pair[0] in invertedIndex.keys():
            invertedIndex[pair[0]].append(pair[1])
        else:
            invertedIndex[pair[0]] = [pair[1]]

    for postingList in invertedIndex.values():
        postingList.sort()

    # print(invertedIndex)
    # invertedIndex.sort()
    for key in sorted(invertedIndex.keys()):
        # print("hello")
        print("%s -> %s" % (key, invertedIndex[key]))


if __name__ == '__main__':
    doc1 = "new home sale top forecast"
    doc2 = "home sale rise in july"
    doc3 = "increase in home sale in july"
    doc4 = "july new home sales rise"
    docList = [doc1, doc2, doc3, doc4]
    invertedIndex(docList)
