fun is_prime : x
    i = 2
    i * i <= x ~+
        x % i == 0 ->
            return false
        i += 1
    return true


input : x
print : is_prime : x


# -> if
# =+ for
# ~= while