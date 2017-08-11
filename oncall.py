import datetime

#date parameters
year = 2017
month = 08
day = 26
hour = 13
minute = 00


#start of on-call shift in UTC (YYYY, MM, DD, HH, MM)  Hour and minute are always 13 and 00
oncall_start = datetime.datetime(year, month, day, hour, minute)

#length of shift
days_on_call = 1


def get_elapsed_seconds(oncall_start, now):
	
	elapsed_time = now - oncall_start
	seconds_passed = elapsed_time.seconds
	seconds_passed += elapsed_time.days * 24 * 60 * 60
	
	return int(seconds_passed)

	
	
def calculate_oncall_completion(total_seconds, elapsed_seconds):

	percentage_complete = (elapsed_seconds / total_seconds) * 100.00
	return round(percentage_complete, 3)


def calculate_oncall_time_remaining(total_seconds, elapsed_seconds):
	
	seconds_remaining = total_seconds - elapsed_seconds	
	return seconds_remaining, "seconds remaining"
	


now = datetime.datetime.now()
total_seconds = days_on_call * 24.00 * 60 * 60
elapsed_seconds = get_elapsed_seconds(oncall_start, now)
	
#print calculate_oncall_completion(total_seconds, elapsed_seconds), "% complete with on-call shift"
