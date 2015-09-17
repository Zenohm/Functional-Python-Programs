def time_convert(time_in_seconds):
	units = 'seconds'
	if time_in_seconds//1==0:
		#Subsecond conversions first
		if time_in_seconds<=0.000000000000000000000001:
			time_in_seconds/=0.000000000000000000000001
			units = 'yoctoseconds'
		elif time_in_seconds<=0.000000000000000000001:
			time_in_seconds/=0.000000000000000000001
			units = 'zeptoseconds'
		elif time_in_seconds<=0.000000000000000001:
			time_in_seconds/=0.000000000000000001
			units = 'attoseconds'
		elif time_in_seconds<=0.000000000000001:
			time_in_seconds/=0.000000000000001
			units = 'femtoseconds'
		elif time_in_seconds<=0.000000000001:
			time_in_seconds/=0.000000000001
			units = 'picoseconds'
		elif time_in_seconds<=0.000000001:
			time_in_seconds/=0.000000001
			units = 'nanoseconds'
		elif time_in_seconds<=0.000001:
			time_in_seconds/=0.000001
			units = 'microseconds'
		elif time_in_seconds<=0.001:
			time_in_seconds/=0.001
			units = 'milliseconds'
		elif time_in_seconds<=0.01:
			time_in_seconds/=0.01
			units = 'centiseconds'
	else:
		#Supersecond conversions last
		if time_in_seconds>=440294400000000000:
			time_in_seconds/=440294400000000000
			units = 'universal ages'
		elif time_in_seconds>=31449600000:
			time_in_seconds/=31449600000
			units = 'millennia'
		elif time_in_seconds>=3144960000:
			time_in_seconds/=3144960000
			units = 'centuries'
		elif time_in_seconds>=31449600:
			time_in_seconds/=31449600
			units = 'years'
		elif time_in_seconds>=604800:
			time_in_seconds/=604800
			units = 'weeks'
		elif time_in_seconds>=86400:
			time_in_seconds/=86400
			units = 'days'
		elif time_in_seconds>=3600:
			time_in_seconds/=3600
			units = 'hours'
		elif time_in_seconds>=60:
			time_in_seconds/=60
			units = 'minutes'
	return str(time_in_seconds)+' '+units
