sentence = str(input("Enter a sentence: ")).lower()
words = []

def split_sentence(sentence):
    global words

    words = sentence.split()
    return words

def reversing():
    global words
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

split_sentence(sentence)
reversed_sentence = reversing()
print("Original sentence:", sentence)
print("Reversed sentence:", reversed_sentence)

