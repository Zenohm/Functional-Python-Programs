def analyzeWeatherData():
    import NaiveBayer as NB
    import getWeatherData as gWD
    data = open("OpenOrImpededSchoolInfo.txt").read()
    data = '['+data[1:]+']'
    try:
        inputVector = gWD.getWeatherData()
    except:
        return "Unable to connect."
    inputVector.append('?')
    summaries = NB.summarizeByClass(data)
    output = NB.predict(summaries,inputVector)
    if output == 4:
        data = open("CloseOrDelaySchoolInfo.txt").read()
        data = '['+data[1:]+']'
        summaries = NB.summarizeByClass(data)
        output = NB.predict(summaries,inputVector)
        if output == 5:
            data = open("2HourOr3HourDelaySchoolInfo.txt").read()
            data = '['+data[1:]+']'
            summaries = NB.summarizeByClass(data)
            output = NB.predict(summaries,inputVector)
    return output

def prediction(condition):
    print('Based on current conditions, school will be ')
    if condition == 0:
        return 'closed'
    elif condition == 1:
        return 'open'
    elif condition == 2:
        return 'delayed for 2 hours'
    elif condition == 3:
        return 'delayed for 3 hours'
    else:
        return 'doing something...'
