with open('Books/frankenstein.txt') as f:
    text = f.read()
    # print(text)

def word_count():
    words = text.split()
    count = len(words)
    return count

def letter_count():
    words = text.lower()
    chars = {}
    for word in words:
        for char in word:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

    chars_org = sorted(chars.items())

    char_dict = {}
    cd_index = 0
    for t in chars_org:
            char_dict[t[0]] = t[1]
    return char_dict

def print_report():
    chars_dict = letter_count()
    chars_dict_sorted = {}
    c_d_s_keys = sorted(chars_dict, key=chars_dict.get, reverse=True)
    for k in c_d_s_keys:
        chars_dict_sorted[k] = chars_dict[k]
    chars = []
    for char in chars_dict_sorted:
        if char.isalpha():
            chars.append(char)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count()} words found in the document\n")
    for char in chars:
        print(f"The '{char}' character was found {chars_dict[char]} times")
    print("\n--- End of Report")

print_report()
