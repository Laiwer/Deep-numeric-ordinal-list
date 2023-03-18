def create_deep_number_list(n):
    number_list = [i for i in range(1, n+1)]
    deep_list = [*number_list]
    for _ in range(n-1):
        number_list = number_list[:-1]
        deep_list = [*number_list, deep_list]
    return deep_list


def see_deep_number_list(n, deep_list):
    output = deep_list
    print(deep_list)
    for i in range(n):
        if i == n-1:
            print(f"{output}" + ("]"*(n-1)))
        else:
            print(f"{output[:-1]}"[:-1] + ",")
            output = output[-1]


if __name__ == "__main__":
    n = int(input("Введите число: "))
    array = create_deep_number_list(n)
    see_deep_number_list(n, array)