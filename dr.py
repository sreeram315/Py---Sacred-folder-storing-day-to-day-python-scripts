# proprietary to BEERA // DO NOT COPY
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
	a=split_title_and_name(person)
	b=lambda x: x.split()[0] + ' ' + x.split()[-1]
	
	print(a==b(person))

#option 2
print(list(map(split_title_and_name, people)) == list(map(b,people)))
