import random
when = ['A long time ago', 'Last week', 'Yesterday', 'On 20th Jan']
who = ['A rabit', 'A elephant', 'A turtle', 'A dog']
name = ['Ali', 'Miriam', 'Daniel', 'Starwalker']
residence = ['India', 'Germany', 'England', 'Barcelona']
went = ['Laundry', 'School', 'University', 'Cinema']
happened = ['Eats a burger', 'Makes a lot of friends', 'Found a key', 'Wrote a book', 'Solved a mystery']
print (random.choice(when) + ", " + random.choice(who) + " named " + random.choice(name) + " that lived in " + random.choice(residence) + " went to the " + random.choice(went) + " and " + random.choice(happened) + ".")