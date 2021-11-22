"""Restaurant rating lister."""


# put your code here
scores = open('scores.txt', "a")

resturant = input('Please enter a resturant name: ')
score = input('What would you rate them from 1 to 5: ')

newRes = resturant + ':' + str(score) + '\n'

scores.write(newRes)

scores.close()


newScores = open('scores.txt', "r")

for line in sorted(newScores):
    print(line)

newScores.close()