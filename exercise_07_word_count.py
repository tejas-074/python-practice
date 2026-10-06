def count_words(sentence):
    counts = {}
    def count_words(sentence):
        counts = {}
    
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(count_words("pass fail pass pass fail"))
print(count_words("a b a c b a"))
print(count_words("Login login LOGIN"))