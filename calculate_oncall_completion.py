import oncall

percentage_complete = oncall.calculate_oncall_completion(oncall.total_seconds, oncall.elapsed_seconds)

if (percentage_complete >= 0 and percentage_complete <= 100):
	print percentage_complete, "% complete with on-call shift"
else:
	print "I am not on-call"