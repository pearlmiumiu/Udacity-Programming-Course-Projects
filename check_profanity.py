def read_text():
	quotes=open("C:\detect_profanity\movie_quotes.txt")
	contents_of_file=quotes.read()
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection=urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output=connection.read()

	connection.close()
	if "true" in output:
		print "Profanity alert"
	elif "False" in output:
		print "this document has no curse words!"
	else:
		print "could not scan the file properly!"

read_text()

