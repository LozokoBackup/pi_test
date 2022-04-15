import random
import textwrap

from backend.configs.categories import Categories
from backend.services.article_summary_service import ArticleSummaryService
from backend.services.wikipedia_service import WikipediaService


class QuestionService:
    def __init__(self):
        self.categories = list(Categories.categories.items())
        self.wikipedia_service = WikipediaService()
        self.article_summary_service = ArticleSummaryService()

    def new_question(self):
        category = random.choice(self.categories)
        words = open(category[1], 'r').readlines()
        answers = random.sample(words, 4)
        right_answer = answers[random.randint(0, 3)]
        refactored_summary = self.form_question_body(right_answer)
        self.form_question(category[0], answers, right_answer, refactored_summary)

    def form_question_body(self, article):
        article = self.wikipedia_service.get_article_title(article)
        summary_raw = self.wikipedia_service.get_article_summary(article)
        refactored_summary = self.article_summary_service.remove_answer_from_question(summary_raw, article)
        return refactored_summary

    def form_question(self, category, answers, right_answer, refactored_summary):
        print(f"New question from {category} category\n")
        print(textwrap.fill(refactored_summary, width=140))
        print("this is the definition of:\n")
        print(f"1:{answers[0]}2:{answers[1]}3:{answers[2]}4:{answers[3]}")
        typed_answer = None
        try:
            typed_answer = input("Write your answer here:")
            user_answer = answers[int(typed_answer)-1]
        except ValueError:
            user_answer = typed_answer + '\n'
            print("\nYou can just write a number but full answer is also ok")
        if user_answer == right_answer:
            print("\nGreat! Your answer is correct!\n\n\n")
        else:
            print(f"\nYou stupid! The right answer is {right_answer}\n\n\n")



