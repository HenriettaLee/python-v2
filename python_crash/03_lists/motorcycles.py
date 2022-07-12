motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

print('-----------------------------')
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

print('-----------------------------')
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

print('-----------------------------')
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


print('-----------------------------')
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
first_owned=motorcycles.pop(1)
print(f'The first motocycle I owned was a {first_owned.title()}')

print('-----------------------------')
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

'''
在列表中添加元素
append: 添加到末尾
insert: 可在列表任何位置添加新元素


从列表中删除元素
del:del语句可以删除任何位置处的列表元素，条件是知道其索引。
pop:pop()删除列表末尾的元素，并可以接着使用它。
pop(index):可以使用pop()删除列表中任意位置的元素。
remove: 根据值删除元素.只删除第一个指定的值

'''