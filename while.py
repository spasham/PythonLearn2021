#book cricket - flip a book of 30 pages till you score 500

import random
flips = []

score = 0
while score < 500:
    runs = random.randint(1,30)
    score = score + runs
    flips.append(runs)
    
print('Total Flips', len(flips), 'Total Score is', score, 'flips are', flips) 

