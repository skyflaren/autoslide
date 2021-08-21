import yake
from textblob import TextBlob
text= 'Your text goes here'
blob = TextBlob(text)
print(blob.noun_phrases)

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
        return self.keywords

class KeywordAnalyzer2:
    def __init__(self):
        self.text = ""
        self.keywords = ""

    def analyze_text(self, text):
        self.text = text
        self.keywords = TextBlob(text)
        return self.keywords