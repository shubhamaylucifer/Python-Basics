def first_function():
    print('This is my first function.')

def second_function(num):
    print(f"Is the number divisible by 3 ? {num % 3 ==0}")

def third_function(num1, num2, num3 = 10):
    print(f"My parameters are {num1},{num2},{num3}")

def function_with_return(num):
    if num % 2 == 0:
        return num ** 3
    else:
        return num ** 2
    
def function_with_multiple_return_value(data):
    split_data = data.split(",")    
    len_split_data = len(split_data)
    return len_split_data, split_data

first_function()
second_function(21)
second_function(20)

third_function(5,7,9)
third_function(100,200)

third_function(num3=100,num1=25, num2= 50)

print(function_with_return(4))
print(function_with_return(5))

print(function_with_multiple_return_value('abc,def,ghi'))
(size,type) = function_with_multiple_return_value('abc,def,ghi')

print(f" The size is {size} and type is {type}")


