#filter
productos=[1,2,3,4,8,9,10]
baratos= filter(lambda x:x<5, productos)
print(list(baratos))
