# stat_tools.py - Pass a list of numbers and get mean, variance, and standard deviation

# TODO - Error-checking that parameter provided was a list
# TODO - Error-checking that list was provided as a list of numbers

def mean(numberList):
    return sum(numberList) / len(numberList)

def differenceFromMean(numberList):
    m = mean(numberList)
    return [a - m for a in numberList]    

def squaredDiffs(numberList):
    return [a ** 2 for a in differenceFromMean(numberList)]

def variance(numberList):
    sDiff = squaredDiffs(numberList)
    return sum(sDiff) / len(sDiff)

def standardDeviation(numberList):
    import math
    # TODO - write try/exception in case math package not installed
    """try:
        import math
    except:
    """
    return math.sqrt(variance(numberList))
