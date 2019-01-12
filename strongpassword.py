user = raw_input("take a password")
if len(user) > 6 and len(user) < 16:
	if "$" in user:
		if "2" in user or "8" in user:
				if "A" in user or "z" in user:
						print "Strong Password hai"
else:
	print "strong password nhi hai"
