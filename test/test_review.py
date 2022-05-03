import unittest
from app.models import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.new_review = Review(12345,'Review for movies','https://image.tmdb.org/t/p/w500/jdjdjdjn','This movie is the best thing since sliced bread')
        # self.userRachel = User(username = 'James',password ='rachel',email='rachel@gmail.com')
    def test_init(self):
        self.assertEqual(self.new_review.movie_id,12345)
        self.assertEqual(self.new_review.title,"Review for movies")
        self.assertEqual(self.new_review.imageurl,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEqual(self.new_review.review,"This movie is the best thing since sliced bread")
    def test_save_review(self):
        self.new_review.save_review()
        self.assertEqual(len(Review.all_reviews),1)
    def tearDown(self):
        Review.all_reviews = []
    def test_get_review_by_id(self):
        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)