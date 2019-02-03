# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

#Change "Hanna" to "Hannah"
people[0] = 'Hannah'

#Change "Geoffrey" to "Jeffrey"
people[-2] = people[-2].replace('Geoffrey', 'Jeffrey')

#Change "aparna" to "Aparna" (capitalize it)
people[-1] = people[-1].capitalize()

print(people)