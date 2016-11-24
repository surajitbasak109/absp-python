#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
	'Andaman and Nicobar Islands': 'Port Blair',
	'Andhra Pradesh': 'Hyderabad',
	'Arunachal Pradesh': 'Itanagar',
	'Assam': 'Dispur',
	'Bihar': 'Patna',
	'Chandigarh': 'Chandigarh[c]',
	'Chhattisgarh':	'Naya Raipur[d]',
	'Dadra and Nagar Haveli': 'Silvassa',
	'Daman and Diu': 'Daman',
	'National Capital Territory of Delhi': 'New Delhi',
	'Goa': 'Panaji[e]',
	'Gujarat': 'Gandhinagar',
	'Haryana': 'Chandigarh',
	'Himachal Pradesh':'Shimla',
	'Jammu and Kashmir': 'Srinagar(S), Jammu(W)',
	'Jharkhand': 'Ranchi',
	'Karnataka': 'Bengaluru',
	'Kerala':'Thiruvananthapuram',
	'Lakshadweep': 'Kavaratti',
	'Madhya Pradesh': 'Bhopal',
	'Maharashtra': 'Mumbai[g]',
	'Manipur': 'Imphal',
	'Meghalaya': 'Shillong',
	'Mizoram': 'Aizawl',
	'Nagaland': 'Kohima',
	'Odisha': 'Bhubaneswar',
	'Puducherry': 'Puducherry',
	'Punjab': 'Chandigarh',
	'Rajasthan': 'Jaipur',
	'Sikkim': 'Gangtok[j]',
	'Tamil Nadu': 'Chennai[k]',
	'Telangana': 'Hyderabad',
	'Tripura': 'Agartala',
	'Uttar Pradesh': 'Lucknow',
	'Uttarakhand': 'Dehradun[l]',
	'West Bengal': 'Kolkata'
}

# Generate 35 quiz files.
for quizNum in range(36):
	# Create the quiz and answer key files.
	quizFile = open('india/capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('india/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
	# Write out the header for the quiz.
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
	quizFile.write('\n\n')
	# Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)
	# Loop through all 50 states, making a question for each.
	# Get right and wrong answers
	for questionNum in range(50):
		# Get right and wrong answers.
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		# Write the question and the answer options to the quiz file.
		quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, 	states[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')
		# Write the answer key to a file.
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()
