string_ex = "hello world"
string_ex2 = "klk"

print(string_ex.count("l"))
string_ex = string_ex.upper()
print(string_ex)
string_ex = string_ex.lower()
print(string_ex)
print(string_ex.index('l'))  # finds first instance of letter -> error if DNE
print(string_ex.endswith("world"))  # can end with the full word
print(string_ex.endswith("d"))   # can end with the last letter
print(string_ex.strip(" "))
print(string_ex.strip(" "))  # removes leading and trailing spaces
print(string_ex.replace("hello", "klk"))
print(string_ex)
print(string_ex.split())
print(string_ex.find("l"))  # finds first index of letter returns -1 if DNE
string_ex3 =", ".join([string_ex2, string_ex])
print(string_ex3)
