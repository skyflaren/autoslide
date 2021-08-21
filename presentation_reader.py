from pptx import Presentation
from pprint import pprint
from keyword_analyzer import KeywordAnalyzer, KeywordAnalyzer2
from webscraper import ImageScraper
import os

if __name__ == "__main__":
    prs = Presentation("cheetah.pptx")
    # kw_analyzer = KeywordAnalyzer(max_ngram_size=2, keyword_count=3)
    kw_analyzer = KeywordAnalyzer2()
    scraper = ImageScraper(per_page=5, quality="thumb")
    queries = [[] for _ in prs.slides]

    # Opening powerpoint and extracting keywords
    print("cheeto")
    print("----------------------")

    for i, slide in enumerate(prs.slides):
        print("Slide #", i)
        print("----------------------")

        text = ""
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += (shape.text+"\n")
        print("Text: ")
        print(text.strip())
        keywords = kw_analyzer.analyze_text(text)
        print("Keywords: ")
        print(keywords)

        queries[i] = [x[0] for x in keywords]
    print(queries)

    # Getting images for keywords
    scraper.download_images(queries)




