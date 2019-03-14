# Let's take a different approach to film recommendations: create the same variables containing your
# potential film recommendations and then ask the user to rate their
# appreciation for 1. documentaries 2. dramas 3. comedies on a scale from one to five.
# If they rate documentaries four or higher, recommend the documentary.
# If they rate documentaries 3 or lower but both comedies and dramas 4 or higher, recommend the dramedy.
# If they rate only dramas 4 or higher, recommend the drama.
# If they rate just comedies 4 or higher, recommend the comedy.
# Otherwise, recommend a good book.

documentary = 'What whwe do in the Shadows'
drama = 'Benjamin Button'
comedy = 'Mars Attacks'
dramedy = 'The Office'

print("How would you rate documentaries? (Scale of 1 to 5)")

doc_rating = int(input())

print("How would you rate dramas? (Scale of 1 to 5)")

drama_rating = int(input())

print("How would you rate comedies? (Scale of 1 to 5)")

com_rating = int(input())

if doc_rating >= 4:
    print(f"Film recommended: {documentary}")
elif doc_rating <= 3 and drama_rating >= 4 and com_rating >= 4:
    print(f"Film recommended: {dramedy}")
elif doc_rating <= 3 and drama_rating >= 4 and com_rating <= 3:
    print(f"Film recommended: {drama}")
elif doc_rating <= 3 and drama_rating <= 3 and com_rating >= 4:
    print(f"Film recommended: {comedy}")
else:
    print("You should try reading a book.")
