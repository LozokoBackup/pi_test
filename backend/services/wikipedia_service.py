import wikipedia


class WikipediaService:
    def get_article_title(self, word):
        return wikipedia.search(word)[0]

    def get_article_summary(self, word):
        try:
            summary = wikipedia.summary(word, auto_suggest=False, redirect=True)
        except wikipedia.DisambiguationError as e:
            summary = wikipedia.summary(e.options[0], auto_suggest=False)
        if len(summary.split('\n')[0]) < 200:
            return "\n".join(summary.split('\n')[0:2])
        else:
            return summary.split('\n')[0]

