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
        
    def test_words_with_apostrophes(self):
        text = "powieść jules'a verne'a"
        result = cap.just_do_it(text)
        self.assertEqual(result, "Powieść Jules'a Verne'a")
        
    def test_words_with_quotes(self):
        text = "Martwiły się inne kaczki: \"Co będzie z takiej dziwaczki?\""
        result = cap.just_do_it(text)
        self.assertEqual(result, "Martwiły Się Inne Kaczki: \"Co Będzie Z Takiej Dziwaczki?\"")
        
if __name__ == '__main__':
    unittest.main()
