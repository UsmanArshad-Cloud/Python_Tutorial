words = ["apple", "banana", "grape", "kiwi", "orange", "watermelon", "mango"]
def ContainsVowel(a):
    vowels = 'aeiouAEIOU'
    return any(char in vowels for char in a)
vowels=list(filter(lambda x:len(x)>5 and ContainsVowel,words))
print(vowels)

