import survey
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)
outcomes = 0
first_babies = []
first_length = []
other_babies = []
other_length = []
for preg in table.records:
	outcomes += preg.outcome
	if preg.outcome == 1:
		first_babies.append(preg.outcome)
		first_length.append(preg.prglength)
	else:
		other_babies.append(preg.outcome)
		other_length.append(preg.prglength)
print 'Number of live births', outcomes
print 'First babies', sum(first_babies)
print 'Other babies', sum(other_babies)
print 'First baby average pregnancy length', sum(first_length) / len(first_length)
print 'Other baby average pregnancy length', sum(other_length) / len(other_length)
