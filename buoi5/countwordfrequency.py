def count_word_frequency(words):
    words_count = {word: words.count(word) for word in words}
    print(words_count)


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)
