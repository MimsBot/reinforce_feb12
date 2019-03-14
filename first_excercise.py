#Think of a documentary, a drama, a comedy, and a dramedy. Store the titles of these films in variables. Ask the user if they enjoy
#1. documentaries 2. dramas 3. comedies. If they answer yes to documentaries, display a message recommending the documentary to them.
#If they answer no to documentaries but yes to dramas and comedies, recommend the dramedy. If they answer yes to only dramas, recommend
#the drama. If they say yes to only comedies, recommend the comedy. If they answer no to all three, recommend a good book instead.


documentary = 'What we do in the Shadows'
drama = 'Benjamin Button'
comedy = 'Mars Attacks'
dramedy = 'The Office'

print('Do you like documentaries?')
# returns first lowercase letter of string (y or n)
documentaries_response = input().lower()[0]
print('Do you like dramas?')
drama_response = input().lower()[0]
print('Do you like comedies?')
comedy_response = input().lower()[0]

if (documentaries_response == 'y'):  # if they choose doc then it recommends
    print('I would recommend {}!'.format(documentary))
# if they dont like docs AND like dramas and comedies - print this
elif (documentaries_response == 'n') and (drama_response == 'y') and (comedy_response == 'y'):
    print("I would recommend {}!".format(dramedy))
elif (drama_response == 'y') and (comedy_response == 'n'):
    print("I would recommend {}!".format(drama))
elif (drama_response == 'n') and (comedy_response == 'y'):
    print("I would recommend {}!".format(comedy))
else:  # used to end the loop and suggest a book instead
    print('Try a book instead...')
