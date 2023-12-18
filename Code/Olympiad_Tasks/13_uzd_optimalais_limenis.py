import doctest


def funkcija_trapece_2(punkta_x, punkta_y: float) -> int:
  """
    Funkcija, kas pārbauda, kur atrodas lietotājs ievadītais punkts.

    Funkcija atgriež sekojošos rezultātus:
        1 - Punkts atrodas iekšā.
        2 - Punkts atrodas uz robežlinijam.
        3 - Punkts atrodas ārpus.

    >>> funkcija_trapece_2(5, -4)
    1
    >>> funkcija_trapece_2(4.5, -0.725)
    2
    >>> funkcija_trapece_2(-2, 4)
    1
    >>> funkcija_trapece_2(-3, 4)
    1
    >>> funkcija_trapece_2(-4, 2)
    2
    >>> funkcija_trapece_2(5, 2)
    2
    >>> funkcija_trapece_2(3, 2)
    2
    >>> funkcija_trapece_2(4, 2)
    2
    >>> funkcija_trapece_2(-4, 1)
    3
    >>> funkcija_trapece_2(-3, 1)
    3
    >>> funkcija_trapece_2(2, -2)
    3

    """
  side = punkta_y == -3
  side_1 = punkta_y == 2
  side_2 = punkta_y == round(-4.55 * punkta_x + 19.75, 3)
  side_3 = punkta_y == round(2.5 * punkta_x + 17.5, 3)
  side_4 = punkta_y == round(-1.30 * punkta_x - 9.1, 3)

  if side or side_1 or side_2 or side_3 or side_4:
    return 2
  elif punkta_x >= -7 and punkta_x <= 3.9 and punkta_y >= -3 and punkta_y <= 2 and not (
      side or side_1 or side_2 or side_3 or side_4):
    return 3
  else:
    return 1


doctest.testmod(verbose=True)

input_x = float(input("Ievadiet punktu x: "))
input_y = float(input("Ievadiet punktu y: "))

if funkcija_trapece_2(input_x, input_y) == 1:
  print("Figūras ārpusē.")
elif funkcija_trapece_2(input_x, input_y) == 2:
  print("Robežlinijā")
else:
  print("Figūras iekšā.")
