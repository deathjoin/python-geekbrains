# Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.

fruits0 = ['apple', 'banana', 'orange']
fruits1 = ['apple', 'cherry', 'orange']

print([f for f in fruits0 for fa in fruits1 if f == fa])
