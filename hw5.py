from collections import Counter


class CountVectorizer:
    """
    Возвращает лист уникальных слов и кол-во их появлений в листе строк
    """
    def __init__(self):
        self._unique_words = []
        self._matrix = []

    def _preproc(self, sample_text: list) -> list:
        """
        Возвращает лист листов слов, переведенных в нижний регистр,
        и заполняет self._unique_words
        """
        set_of_words = set()
        processed_text = []
        for i in range(len(sample_text)):
            if not isinstance(sample_text[i], str):
                raise ValueError(f'На вход ожидается лист строк,\
                                   вы передали{type(sample_text[i])}')
            sentence = sample_text[i].lower()
            processed_text.append(sentence.split())
        set_of_words.update(*processed_text)
        self._unique_words = sorted(list(set_of_words))
        return processed_text

    def fit_transform(self, sample_text: list) -> list:
        processed_text = self._preproc(sample_text)
        for sentence in processed_text:
            c = Counter(sentence)
            sentence_count_words = [c[word] for word in self._unique_words]
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
    print(count_matrix, vectorizer.get_feature_names(), sep='\n')
