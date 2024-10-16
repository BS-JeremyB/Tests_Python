from validation_email import email_valide

def test_email_valide():
    assert email_valide("johndoe@mail.com")
    assert not email_valide("johndoe@mail")
    assert not email_valide("@mail.com")