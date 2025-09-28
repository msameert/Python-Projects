"""Even num gen using iterators and generators"""

def even_num_gen():
    num = 0
    while True:
        yield num     #yield instead of return
        num += 2

f = even_num_gen()


n = int(input("Enter The number you want even numbers till: "))
print("Here are your even numbers :")
for i in range(n):
    print(next(f))  #generator used here