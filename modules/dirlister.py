def run(**args):
	print "{*} In dirlister module."
	files = os.dirlister(".")

	return str(files)