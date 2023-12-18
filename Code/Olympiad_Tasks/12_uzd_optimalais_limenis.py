from doctest import testmod

def funkcija_aplis_kreisi(x_cord, y_cord: float):
    """
    Funkcija, kas pārbauda, kur atrodas lietotājs ievadītais punkts.

    Funkcija atgriež sekojošos rezultātus:
        1 - Punkts atrodas iekšā.
        2 - Punkts atrodas uz robežlinijam.
        3 - Punkts atrodas ārpus.

    >>> funkcija_aplis_kreisi(0,0)
    1
    >>> funkcija_aplis_kreisi(-6,2)
    1
    >>> funkcija_aplis_kreisi(2,0)
    1
    >>> funkcija_aplis_kreisi(-4,1)
    2
    >>> funkcija_aplis_kreisi(-2,3)
    2
    >>> funkcija_aplis_kreisi(-6,3)
    2
    >>> funkcija_aplis_kreisi(-5,4)
    3
    >>> funkcija_aplis_kreisi(-4,3)
    3
    >>> funkcija_aplis_kreisi(-5,3)
    3
    >>> funkcija_aplis_kreisi(-4,2)
    3

    """
    circle_radius = 2
    x_middle = -4
    y_middle = 3

    distance_squared = (x_cord - x_middle) ** 2 + (y_cord - y_middle) ** 2

    if distance_squared <= circle_radius ** 2 and y_cord <= 5 * x_cord + 33:
        if (distance_squared == circle_radius ** 2) or (y_cord == 5 * x_cord + 33):
            return 2
        else:
            return 3
    else:
        return 1


testmod(verbose=True)

input_x = float(input("Ievadiet koordinatu x: "))
input_y = float(input("Ievadiet koordinatu y: "))
if funkcija_aplis_kreisi(input_x, input_y) == 1:
    print("Figūras ārpusē.")

elif funkcija_aplis_kreisi(input_x, input_y) == 2:
    print("Robežlinijā")

else:
    print("Figūras iekšā.")