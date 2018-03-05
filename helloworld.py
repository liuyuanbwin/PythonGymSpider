import time
key_test = {'key':'a test','key':'123'}
key_test.update({'key1':'ttt'})
del key_test['key']
print(key_test)
print(time.clock())
num_list = [6,5,8,7,2,1,9,45]
print(sorted(num_list))
b = [i for i in range(1,11)]
print(b)
print(time.clock())
