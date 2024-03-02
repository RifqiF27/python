# Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:
#   3 -->    15  (  3 * 5¹)
#  10 -->   250  ( 10 * 5²)
# 200 --> 25000  (200 * 5³)
#   0 -->     0  (  0 * 5¹)
#  -3 -->   -15  ( -3 * 5¹)

def multiply(n):
    power = len(str(n))
    if n < 0:
        powers = abs(n)
        power = len(str(powers))
        return n*(5**power)
    elif n >= 0:
        return n * (5**power)


print(multiply(5))
print(multiply(10))
print(multiply(-2))
print(multiply(0))
