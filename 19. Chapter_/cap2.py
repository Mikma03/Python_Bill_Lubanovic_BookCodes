def just_do_it(text):
    """
    >>> just_do_it('kaczka')
    'Kaczka'
    >>> just_do_it('opodal krzaczka mieszkała kaczka dziwaczka')
    'Opodal Krzaczka Mieszkała Kaczka Dziwaczka'
    >>> just_do_it("powieść jules'a verne'a")
    "Powieść Jules'a Verne'a"
    """
    from string import capwords
    return capwords(text)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
# znuaba1s