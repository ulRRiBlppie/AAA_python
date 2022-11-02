
class CountVectorizer:
    """
    Возвращает лист уникальных слов и кол-во их появлений в листе строк
    """
    def __init__(self):
        self._unique_words = []
        self._matrix = []

    def fit_transform(self, sample_text: list) -> list:

        for sentence in sample_text:
            if not isinstance(sentence, str):
                raise ValueError(f'На вход ожидается лист строк,\
                                    вы передали{type(sentence)}')

            words_in_sentence = [x.lower() for x in sentence.split()]
            for word in words_in_sentence:
                if word not in self._unique_words:
                    self._unique_words.append(word)

        for sentence in sample_text:
            words_in_sentence = [x.lower() for x in sentence.split()]
            sentence_count_words = []
            for unique_word in self._unique_words:
                sentence_count_words.append(
                                    words_in_sentence.count(unique_word)
                                    )
            self._matrix.append(sentence_count_words)

        return self._matrix

    def get_feature_names(self) -> list:
        return self._unique_words


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix, vectorizer.get_feature_names())
