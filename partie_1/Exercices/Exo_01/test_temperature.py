from temperature import convertisseur_celsius_fahrenheit

def test_convertisseur_celsius_fahrenheit():
    try:
        assert convertisseur_celsius_fahrenheit(0) == 32
        print("0 celsius = 32 fahrenheit : OK")
    except AssertionError:
        print("0 celsius = 32 fahrenheit : FAIL")

    try:
        assert convertisseur_celsius_fahrenheit(-12) == 10.399999999999999
        print("-12 celsius = 10.399999999999999 fahrenheit : OK")
    except AssertionError:
        print("-12 celsius = 10.399999999999999 fahrenheit : FAIL")


test_convertisseur_celsius_fahrenheit()