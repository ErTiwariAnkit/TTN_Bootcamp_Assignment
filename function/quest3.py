def fun1(*num):
    for i in num:
        print(i)
def argument_pass(*num2):
    fun1(*num2)
argument_pass(20,40,60)
argument_pass(80,10)