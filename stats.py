def get_num_words(content):
    count = len(content.split())
    return count


def char_count(content):
    count = {}

    for c in content:
        ch = c.lower()
        if ch not in count:
            count[ch] = 0
        count[ch] += 1

    return count


def chars_descending(char_count):
    count = []
    for key, val in char_count.items():
        count.append({"char": key, "num": val})

    count.sort(key=lambda x: x["num"], reverse=True)
    return count
