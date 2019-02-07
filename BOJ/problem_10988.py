word = input()


def is_palindrome(text: str) -> int:
    mid = len(text) // 2
    if len(text) % 2 == 1:
        return 1 if text[:mid] == text[len(text):mid:-1] else 0
    else:
        return 1 if text[:mid] == text[len(text):mid - 1:-1] else 0


print(is_palindrome(word))
