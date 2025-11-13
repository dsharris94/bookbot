def get_word_count(f):
    return len(f.split())
    
def count_characters(b):            #pulls in text of book as one string
    char_count = {}                 #defines char_count as a dictionary
    for char in b:                  #iterates over book_text. char = 'i'th value in book_text
            char = char.lower()     #converts char to lower for comparison and input to dictionary
            if char in char_count:  #increments if char key already exists
                char_count[char] += 1
            else:                   #adds char key at 1 if key does not already exist
                char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def book_dic_sorter(d):
    sorted_list = []
    for char in d:
        count = d[char]
        dict_item = {
             "char": char,
             "num": count,
        }
        sorted_list.append(dict_item)
    return sorted_list