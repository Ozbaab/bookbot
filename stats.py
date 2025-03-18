def num_of_words(text):
    split = text.split()
    return len(split)

def count_characters(string):
    string_count = {}
    string_lower = string.lower()
    for c in string_lower:
        if c not in string_count:
            string_count[c] = 1
        else:
            string_count[c] += 1
    return string_count

def sort_on(dict):
    return dict["Count"]

def print_pretty(string_count):
    pretty_list = []
    for k, v in string_count.items():
        if k not in pretty_list:
            pretty_list.append({"Character": k, "Count": v})
    pretty_list.sort(reverse=True, key=sort_on)
    return pretty_list