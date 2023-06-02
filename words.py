def print_upper_words(arr, letters):
        for item in arr:
            if any(item.startswith(letters[val]) for val in range(len(letters))):
                print(item.upper())
            else:
                print("doesn't work!")

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   letters=["h", "y"])