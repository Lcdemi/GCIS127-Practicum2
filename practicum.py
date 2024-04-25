"""
Implement your solution to the practicum problems in this file.

LUKE DEMI
"""

# Used in the "phonetic translation" problem. DO NOT MODIFY THIS LIST.
PHONETIC_ALPHABET = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
    "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", 
    "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", 
    "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]

def ascii_tuple(word):
    new_tuple = (ord(word[i]) for i in range(len(word))) #for some reason not working
    return new_tuple

def contains_all(a_list, b_list):
    for element in b_list:
        if element not in a_list:
            return False
    return True

def fish_sort(unsorted_list):
    copy = []
    for element in unsorted_list:
        copy.append(element)
    sorted_list = []
    for _ in range(len(unsorted_list)):
        current_min = copy[0]
        current_min_index = 0
        for index in range(len(copy)):
            #print(index) test code
            if copy[index] < current_min:
                current_min = copy[index]
                current_min_index = index
                #print(current_min_index) test code
        copy.pop(current_min_index)
        #print(copy) test code
        sorted_list.append(current_min)
        #print(sorted_list) test code
    print(len(unsorted_list))
    return sorted_list

def phonetic_translation(String):
    counter = 0
    string_list = []
    for char in String:
        for word in PHONETIC_ALPHABET:
            if char.lower() == word[0].lower():
                string_list.insert(counter, word)
        counter += 1
    return string_list

def is_pangram(String):
    String = String.lower()
    letter_list = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(letters)):
        letter_list.append(letters[i])
    #print(letter_list) test code

    found_letters = 0
    for char in String:
        if char in letter_list:
            found_letters += 1
            letter_list.remove(char)
    
    if len(letter_list) == 0:
        return True
    return False


def main():
    # print(ascii_tuple("dog"))
    # print(fish_sort([3, 2, 1, 5, 7, 6, 1]))
    print(phonetic_translation("LOVE"))
    # print(is_pangram("The Moon"))

if __name__ == "__main__":
    main()