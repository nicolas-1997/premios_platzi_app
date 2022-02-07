import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse



from .models import Question

def create_a_question(question:str, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question, pub_date=time)

class QuestionModelTest(TestCase):


    def test_was_published_recently_with_future_questions(self):
        """
            was_published_recently returns False for questions whose pub_date is in the future.
        """
        future_question = create_a_question("Who is the best Course Director of Platzi?", 30)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_new_questions(self):
        """
            was_published_recently returns True for questions whose pub_date is in the present.
        """
        time = timezone.now() 
        new_question =  create_a_question("Who is the best Course Director of Platzi?",days=0)
        self.assertIs(new_question.was_published_recently(), True)


    def test_was_published_recently_with_old_questions(self):
        """
            was_published_recently returns False for questions whose pub_date is in the past.
        """
        old_question = create_a_question("Who is the best Course Director of Platzi?", days=-2)
        self.assertIs(old_question.was_published_recently(), False)

class QuestionIndexViewTest(TestCase):

    def test_no_questions(self):
        """If no question exist, an appropiate message is displayed"""

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question(self):
        """
            Question with a pub_date in the future aren´t displayed on the index page.
        """
        create_a_question("future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        

    def test_past_question(self):
        """
            Question with a pub_date in the past are displayed on the index page.
        """
        question = create_a_question(question="past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])