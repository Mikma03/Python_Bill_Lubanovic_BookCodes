def dump(func):
    "Funkcja wyświetlająca wartości argumentów i zwracane wyniki"
    def wrapped(*args, **kwargs):
        print("Nazwa funkcji:", func.__name__)
        print("Wartości argumentów pozycyjnych:", ' '.join(map(str, args)))
        print("Wartości argumentów nazwanych:", kwargs.items())
        output = func(*args, **kwargs)
        print("Wyniki:", output)
        return output
    return wrapped
