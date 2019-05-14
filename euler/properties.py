def is_palindrome(value):
    """
    Tells whether a number is palindromic or not
    Origin : Problem 4
    """
    return str(value) == str(value)[::-1]
