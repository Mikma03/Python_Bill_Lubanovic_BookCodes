start1 = ["raz", "dwa", "trzy"] 
rymy = [
    ("sklep", "schylił łeb"),
    ("ziut", "przeciął drut"),
    ("bom", "chwycił łom"),
    ("gaz", "szybko wlazł"),
    ("siup", "wyniósł łup"),
    ("siad", "głupio wpadł"),
    ("cóż", "siedzi już"),
    ]
start2 = "Mały Jasio"

start1_wielkie_litery = " ".join([słowo.capitalize() + "!" for słowo in start1])
for pierwsza, druga in rymy:
    print(f"{start1_wielkie_litery} {pierwsza.capitalize()}!")
    print(f"{start2} {druga}.")
