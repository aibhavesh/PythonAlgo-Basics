a = 'bhavesh'
print(a)  # Output: bhavesh

print(a.capitalize())  # Capitalizes the first letter. Output: Bhavesh

print(a.casefold())  # Converts the string to lowercase. Output: bhavesh

print(a.center(20, '-'))  # Centers the string within a field of 20 characters, padded with '-'. Output: -------bhavesh-------

print(a.count('h'))  # Counts the occurrences of 'h'. Output: 2

print(a.encode())  # Encodes the string into bytes. Output: b'bhavesh'

print(a.endswith('h'))  # Checks if the string ends with 'h'. Output: True

print(a.find('e'))  # Finds the first occurrence of 'e'. Output: 4

print("Hello, {}".format(a))  # Formats the string using a placeholder. Output: Hello, bhavesh

print(a.index('v'))  # Finds the first occurrence of 'v'. Output: 3

print(a.isalnum())  # Checks if all characters are alphanumeric. Output: True

print(a.isalpha())  # Checks if all characters are alphabetic. Output: True

print(a.isdigit())  # Checks if all characters are digits. Output: False

print(a.islower())  # Checks if all characters are lowercase. Output: True

print("   ".isspace())  # Checks if the string contains only whitespace. Output: True

print(a.istitle())  # Checks if the string is title-cased. Output: False

print(a.isupper())  # Checks if all characters are uppercase. Output: False

print("-".join(["hello", a]))  # Joins a list of strings with a separator. Output: hello-bhavesh

print(a.lower())  # Converts all characters to lowercase. Output: bhavesh

print(a.replace("b", "B"))  # Replaces occurrences of 'b' with 'B'. Output: Bhavesh

print(a.split('e'))  # Splits the string by 'e'. Output: ['bhav', 'sh']

print(a.startswith('b'))  # Checks if the string starts with 'b'. Output: True

print("  bhavesh  ".strip())  # Removes leading and trailing whitespace. Output: bhavesh

print(a.upper())  # Converts all characters to uppercase. Output: BHAVESH
