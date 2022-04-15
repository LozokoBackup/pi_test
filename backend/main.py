from backend.services.questions_service import QuestionService
from web_scraper.web_scraper_animals import ScraperAnimals
import warnings


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    #scraper = ScraperAnimals("./assets/Animals.html")
    #scraper.scrap()
    #scraper.scrap_refactor()
    question_service = QuestionService()
    while True:
        question_service.new_question()
