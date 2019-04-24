import db

_db = db.connect_with_db()


def test_send_greetings():
    name = "Stanisław Brzęczyszczykiewicz"
    greeting = "ąśćźżśę©ß←’æΩŚÐÆÐŊÆĄÐŚŒefe"
    coll = _db["greetings"]

    db.send_greetings(name, greeting)

    document = coll.find_one()
    coll.delete_many({})
    assert name == document['name']
    assert greeting == document['greeting']
