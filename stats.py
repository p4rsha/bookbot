def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content
    
    
def get_num_words(text):
    return len(text.split())


def char_count(text):
    result = {}

    for char in text.lower():
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result


def sort_dict(raw_dict):

    list = []
    for key in raw_dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = raw_dict[key]
        list.append(new_dict)

    def sort_on(items):
        return items["num"]
    
    list.sort(reverse = True , key= sort_on)

    return list


