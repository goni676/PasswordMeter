import re

def find_date(text):
    date_pattern = r'\b(19\d{2}|20[0-1]\d|2023)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])|' \
                   r'(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(19\d{2}|20[0-1]\d|2023)|' \
                   r'(0[1-9]|[12]\d|3[01])(0[1-9]|1[0-2])(19\d{2}|20[0-1]\d|2023)|' \
                   r'(19\d{2}|20[0-1]\d|2023)|' \
                   r'(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])|' \
                   r'(0[1-9]|[12]\d|3[01])(0[1-9]|1[0-2])\b'

    match = re.search(date_pattern, text)
    if match:
        return match.group()



# if contains_date(text):
#     print("The text contains a date.")
# else:
#     print("No date found in the text.")


def contains_mutual_substring(str1, str2):
    str1_lower = str1.lower()
    str2_lower = str2.lower()

    for i in range(len(str1_lower)):
        for j in range(3, len(str1_lower) - i + 1):
            substring = str1_lower[i:i + j]
            if substring in str2_lower:
                return 1, substring

    return 0, ""

