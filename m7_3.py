import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans("","", string.punctuation))
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for filename, words in self.get_all_words().items():
            word_l = word.lower()
            if word_l in words:
                result[filename] = words.index(word_l) +1
        return result

    def count(self, word):
        result = {}
        for filename, words in self.get_all_words().items():
            word_l = word.lower()
            count = words.count(word_l)
            if count > 0:
                result[filename] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('text')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего