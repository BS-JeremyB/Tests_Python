from calculs import add, divide


def test_add():
    try:
        assert add(1, 2) == 3
        print("OK")
    except AssertionError:
        print("FAIL")

    try:
        assert add(3, 0) == 3
        print("OK")
    except AssertionError:
        print("FAIL")

    try:    
        assert add(0, 0) == 0
        print("OK") 
    except AssertionError:
        print("FAIL")

    try:
        assert add(-4, 2) == -2
        print("OK")
    except AssertionError:
        print("FAIL")


def test_divide():
    try:
        assert divide(1, 2) == 0.5
        print("OK")
    except AssertionError:  
        print("FAIL")

    try:
        divide(3, 0) == 0
        print("FAIL")
    except ZeroDivisionError:
        print("OK")
    except Exception:
        print("FAIL")
        
print("test_add")
test_add()
print("test_divide")
test_divide()
