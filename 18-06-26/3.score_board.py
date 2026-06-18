'''
3. Input ball-by-ball runs.
print:
Total score
Number of boundaries
number of dot balls.'''

total_score=0
boundaries=0
dot_balls=0
for i in range(int(input("Enter Number of balls:"))):
    score=int(input("Enter Score of the ball:"))
    if score == 4 or score == 6:
        boundaries+=1
        total_score+=score    
    elif score == 0:
        dot_balls+=1
        total_score+=score
    else:
        total_score+=score

print('Total Score:',total_score)
print('Boundaries',boundaries)
print('Dot Balls',dot_balls)