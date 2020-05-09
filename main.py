
raise_factor = 2400
unacceptable = 0
acceptable = 0.4
meritorious= 0.6

rating = float(input("Enter the rating: "))

if rating == unacceptable:
  performance = "Unacceptable"
elif rating == acceptable:
  performance = "Accetable"
elif rating >= meritorious:
  performance = "meritorious"
else:
  performance = ""

if performance == "":
  print("That wasn't a valid rating")
else:
    print(f"Based on that rating, the performance is {performance}")
    print(f"You will recieve a raise of {rating * raise_factor:.2f}")