import cap2
from nose.tools import eq_

def test_one_word():
    text = 'kaczka'
    result = cap2.just_do_it(text)
    eq_(result, 'Kaczka')
    
def test_multiple_words():
    text = 'opodal krzaczka mieszkała kaczka dziwaczka'
    result = cap2.just_do_it(text)
    eq_(result, 'Opodal Krzaczka Mieszkała Kaczka Dziwaczka')
    
def test_words_with_apostrophes():
    text = "powieść jules'a verne'a"
    result = cap2.just_do_it(text)
    eq_(result, "Powieść Jules'a Verne'a")
    
def test_words_with_quotes():
    text = "Martwiły się inne kaczki: \"Co będzie z takiej dziwaczki?\""
    result = cap2.just_do_it(text)
    eq_(result, "Martwiły Się Inne Kaczki: \"Co Będzie Z Takiej Dziwaczki?\"")
