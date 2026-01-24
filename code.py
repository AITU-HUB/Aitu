nambers = [1,2,3,4,5,6,7,8,9]
squeres = list(map(lambda x: x**2, nambers))
print(squeres)
evens= list(filter(lambda x: x%2 == 0, nambers))
print(evens)
zipped=list(zip(squeres,evens))
print(zipped)
it=iter(nambers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
copy_nambers=nambers.copy()
copy_nambers.append(100)
print(nambers)
print(copy_nambers)



sentence: str = input("Write a sentence: ")

num_letters: int = 0
vowel_counter: int = 0
vowels: str = "aeiouy"

five_letters: str = sentence[:5]
last_letters: str = sentence[-5:]
isPalindrome: bool = sentence.lower() == sentence[::-1].lower()

encoded_bytes = sentence.encode("utf-8")

for i in sentence.lower():
    if i == " ":
        continue
    elif i in vowels:
        vowel_counter += 1
    num_letters += 1

print("First 5 letters:", five_letters)
print("Last 5 letters:", last_letters)
print("Number of letters:", num_letters)
print("Number of vowels:", vowel_counter)
print("Is palindrome:", isPalindrome)
print("UTF-8 encoded bytes:", encoded_bytes)
print("Type:", type(encoded_bytes))
