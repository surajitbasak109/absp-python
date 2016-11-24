#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, re, os
# Create a regex that matches files with the American date format.
datePattern = re.compile(r'''^(.*?)
	((0|1)?\d)-
	((0|1|2|3)?\d)-
	((19|20)\d\d)
	(.*?)$
''', re.VERBOSE)
# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('./absp/dateFile'):
	mo = datePattern.search(amerFilename)
	# Skip files without a date.
	if mo == 'None':
		continue
	# Get the different parts of the filename
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# Form the European-style filename.
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
	# Get the full, absolute file paths.
	absFilepath = os.path.abspath('./absp/dateFile')
	amerFilename = os.path.join(absFilepath, amerFilename)
	euroFilename = os.path.join(absFilepath, euroFilename)
	# Rename the files.
	print('Renaming "%s" to "%s"...\n' % (amerFilename, euroFilename))
	shutil.move(amerFilename, euroFilename) #uncomment after testing
