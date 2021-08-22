import yake
import nltk
from textblob import TextBlob
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

class KeywordAnalyzer:
    def __init__(self, language="en", max_ngram_size=3, deduplication_threshold=0.3, keyword_count=5):
        self.text = ""
        self.keywords = ""
        self.language = "en"
        self.max_ngram_size = max_ngram_size
        self.deduplication_threshold = deduplication_threshold
        self.keyword_count = keyword_count
        self.kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold,
                                                  top=keyword_count, features=None)

    def analyze_text(self, text):
        self.text = text
        self.keywords = self.kw_extractor.extract_keywords(self.text)

        print("Thang:")
        print(self.keywords)

        kw_str = ""
        for x in self.keywords:
            kw_str += f"{x[0]} "

        is_noun = lambda pos: pos[:2] == 'NN'   
        tokenized = nltk.word_tokenize(kw_str)
        self.nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 

        if len(self.nouns) == 0:
            self.nouns = self.keywords

        return self.nouns

class KeywordAnalyzer2:
    def __init__(self):
        self.text = ""
        self.keywords = ""

    def analyze_text(self, text):
        self.text = text
        self.keywords = TextBlob(text)
        return self.keywords

class KeywordAnalyzer3:
    def __init__(self):
        self.text = ""
        self.keywords = []

    def analyze_text(self, text):
        self.text = ""
        self.keywords = keywords(text)
        return keywords(text)