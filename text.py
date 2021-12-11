def some() :
    for num1 in range(3, 8) :
        for num2 in range(15, 20) :
            yield num1, num2
            
for num1, num2 in some():
    with open(f'./classes/{num1}-{num2}.mp4', 'w') as f:
        f.write('')