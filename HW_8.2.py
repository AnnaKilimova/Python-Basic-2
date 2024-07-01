import string
def is_palindrome(text):
    palindrome = ''

    for symbol in text:
        if symbol.isalnum():
            palindrome += symbol.lower()

    if len(palindrome) <= 1:
        return True

    if palindrome[0] != palindrome[-1]:
        return False

    return is_palindrome(palindrome[1:-1])

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")