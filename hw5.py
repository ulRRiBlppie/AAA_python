
class CountVectorizer:
    """
    Возвращает лист уникальных слов и кол-во их появлений в листе строк
    """
    def __init__(self):
        self._dict_of_unique_words = {}
        self._list_of_dict = []
        self._list_of_rows = []


    def fit_transform(self, sample_text: list) -> list:
        for i, sentence in enumerate(sample_text):
            if not isinstance(sentence, str):
                raise ValueError(f'На вход ожидается лист строк,\
                                    вы передали{type(sentence)}')

            words_in_sentence = [x.lower() for x in sentence.split()]
            self._list_of_dict.append({})
            for word in words_in_sentence:
                if word not in self._dict_of_unique_words:
                    self._dict_of_unique_words[word] = 1
                    self._list_of_dict[i][word] = 1
                else:
                    if word not in self._list_of_dict[i].keys():
                        self._list_of_dict[i][word] = 1
                    else:
                        self._list_of_dict[i][word] += 1

        
        self._list_of_rows = [[self._list_of_dict[j].get(word, 0) for word in  self._dict_of_unique_words ] for j in range(i+1)]
        return self._list_of_rows
        

    def get_feature_names(self) -> list:
        return list(self._dict_of_unique_words.keys())


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix, vectorizer.get_feature_names())


