

def holdout_random(input_data, p = 0.1, seed = 11, use_seed = False):
    if use_seed:
        np.random.seed(seed)
    trainId = []
    valId = []
    userAssignment = {}
    itemAssignment = {}
    # initial assignment
    for i in range(len(input_data)):
        u = input_data[i][0]
        v = input_data[i][1]
        # observed in train
        if np.random.random() > p:
            userAssignment[u] = 1
            itemAssignment[v] = 1
            trainId.append(i)
        # assign to val
        else:
            valId.append(i)
    # recheck if any user or item only appeared in val
    newValId = []
    for j in valId:
        u = input_data[j][0]
        v = input_data[j][1]
        if u not in userAssignment or v not in itemAssignment:
            trainId.append(j)
        else:
            newValId.append(j)
    return [input_data[i] for i in trainId], [input_data[i] for i in newValId]

def holdout_domain_random(input_data, p = 0.1, seed = 11, use_seed = False):
    if use_seed:
        np.random.seed(seed)
    print("Random holdout p = " + str(p))
    trainData = dict()
    valData = dict()

    for d, D in input_data.items():
        print("Domain: " + d)
        domainTrain, domainVal = holdout_random(D, p)
        trainData[d] = domainTrain
        valData[d] = domainVal
    return trainData, valData
