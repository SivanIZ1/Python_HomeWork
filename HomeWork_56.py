def multiply_by_two(number):
    result = number * 2
    print(result)
multiply_by_two(5)

def double_length(text):
    length = len(text)
    return length * 2
print(double_length("hello"))

def check_last_char(text):
    last_char = text[-1]
    count_appearances = text.count(last_char)
    if count_appearances > 1:
        return True
    else:
        return False
print(check_last_char("alona"))
print(check_last_char("apple"))