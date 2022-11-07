def build_word_tree_from_sentences(sentence_list):
    root = {}
    for sentence in sentence_list:
        base = root
        for word in sentence.split(' '):
            if not base.get(word):
                base[word]={ }
                base = base [word]
    return root

tree = build_word_tree_from_sentences(["Hello there","Hello world whatsup","Hello world"])
print(tree) 