def decor_result(result_function):
    def dictintion(marks1):
        for i in marks1:
            if i>=75:
                print("dictintion")
        #result_function(marks)
    return dictintion
@decor_result
def result(marks):
    for i in marks:
        if i>=33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")
result([98,87,45,77,34,87])

