s = input("Enter the string: ") 
for i in range(len(s)):
    if i == 2:
        continue
    if s[i] == 'c':
        print(" Found symbol c") 
    print(s[i], end='')
print("\nLine length:", len(s)-1) 
