# for 반복문

a = ['car', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('')

# 복합 자료형을 사용하는 for문
l = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]
for data in l:
    print('이름: %s, 나이: %d' % data)

for name, age in l:
    print('이름: {}, 나이: {}'.format(name, age))

l = [{'name': '둘리', 'age': 10},
     {'name': '마이콜', 'age': 20},
     {'name': '도우넛', 'age': 30}]

for data in l:
    print('이름: %(name)s, 나이: %(age)d' % data)
