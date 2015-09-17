import getWeatherData as gWD
import schoolStatus as sS
data = gWD.getWeatherData()
schoolStatusIdentifier = sS.schoolStatus()
dataOriginal = data
if schoolStatusIdentifier == 1:
	data.append(1)
	file = open("OpenOrImpededSchoolInfo.txt",'a')
	file.write(','+str(data))
	file.close()
data = dataOriginal
if schoolStatusIdentifier != 1:
	data.append(4)
	file = open("OpenOrImpededSchoolInfo.txt",'a')
	file.write(','+str(data))
	file.close()
data = dataOriginal
if not schoolStatusIdentifier:
	data.append(0)
	file = open("CloseOrDelaySchoolInfo.txt",'a')
	file.write(','+str(data))
	file.close()
data = dataOriginal
if schoolStatusIdentifier == 2 or schoolStatusIdentifier == 3:
	data.append(5)
	file = open("CloseOrDelaySchoolInfo.txt",'a')
	file.write(','+str(data))
	file.close()
	data = dataOriginal
	data.append(schoolStatusIdentifier)
	file = open("2HourOr3HourDelaySchoolInfo.txt",'a')
	file.write(','+str(data))
	file.close()