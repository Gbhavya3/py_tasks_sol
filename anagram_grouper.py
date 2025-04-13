def group_anagrams(words):
    result = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in result:
            result[sorted_word].append(word)
        else:
            result[sorted_word] = [word]
    return list(result.values())


words = ["bat", "tab", "tap", "pat", "cat"]
print(group_anagrams(words))
