s = input('Enter s:')
t = input('Enter t:')

left = 0
right = len(t)

points = []

while right <= len(s): 
    if s[left:right] == t:
        points.append(left+1)
    left += 1 
    right += 1 

print(points)
