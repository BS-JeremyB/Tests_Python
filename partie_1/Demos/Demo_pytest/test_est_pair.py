from est_pair import est_pair

def test_est_pair():
    assert est_pair(2) == True
    assert est_pair(3) == False
    assert est_pair(-3) == False
    assert est_pair(0) == True