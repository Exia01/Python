#Adding Donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
for name, donation in donations.items():
    print(donation)
    total_donations += donation

print(total_donations)

#lambda version

total_donations = sum(donation for donation in donations.values())
print(total_donations)