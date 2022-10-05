fun get_max_number : a;b;c

    a > b and a > c ->
        return a

    b > a and b > c ->
        return b

    return c

read : a
read : b
read : c
print : get_max_number : a;b;c