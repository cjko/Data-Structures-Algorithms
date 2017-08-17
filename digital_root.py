def digital_root(n):
    n = int(round(n))
    digit = 0
    while n > 0:
      digit += n%10
      n = (n-digit)/10
    return digit

print(digital_root(14.5))