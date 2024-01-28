# Palindrome
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")

if is_palindrome(something):
    print("It is a palindrome")
else:
    print("It is not a palindrome")