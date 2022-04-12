def calcRisk(vaccine, temp, trips, people):
    if(temp > 98):
        temp = 0.75
    else:
        temp = 0.5
    risk = (vaccine * 0.5) + (temp * 0.25) + \
        (trips * 0.1) + (people * 15)
    if(risk > 1):
        risk = 1
    return risk * 100


def getVax(q):
    val = 0
    if(q[0].booster):
        val = 1
    elif(q[0].dose2 and q[0].booster is None):
        val = 3
    elif(q[0].booster is None and q[0].dose2 is None and q[0].dose1):
        val = 5
    return val
