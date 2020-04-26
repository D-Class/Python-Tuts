integer = 9
print(integer)
print(float(integer))

floatingPointNumber = 2.3
print(floatingPointNumber)
print(int(floatingPointNumber))

string = 'String'
print(string)

my_list = [2, 4.6, 'string']
print(my_list)
my_list[1] = 'd-class'
print(my_list)

my_tuple = 2, 4.6, 'Tuple'
tupleInToList = list(my_tuple)
tupleInToList[2] = 'Updated Tuple'
updatedTuple = tuple(tupleInToList)

for i in updatedTuple:
    print(i)







