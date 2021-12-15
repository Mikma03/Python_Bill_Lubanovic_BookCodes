import unittest
import cap

class TestCap(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_word(self):
        text = 'kaczka'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'Kaczka')

    def test_multiple_words(self):
        text = 'opodal krzaczka mieszkała kaczka dziwaczka'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'Opodal Krzaczka Mieszkała Kaczka Dziwaczka')

if __name__ == '__main__':
    unittest.main()
