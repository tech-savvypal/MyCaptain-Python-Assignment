string=input("Please enter a string:")
def most_frequent(s):
    d=dict()
    for key in s:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d
print(most_frequent(string))

