T = int(input())

for test_num in range(1, T+1):
    F, L = map(int, input().split())
    int_list = list(range(F, L+1))
    str_list = list(map(str, int_list))

    result = 0
    for index, value in enumerate(int_list):
        if '9' in str_list[index]:
            continue

        if value % 9 == 0:
            continue

        result += 1

    print(f'Case #{test_num}: {result}')
