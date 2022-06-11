def parse_cookie(query: str) -> dict:
    cookie_dict = {cookie[0]: cookie[1] for cookie in [data.split('=', 1) for data in query.split(';')]
                   if len(cookie) > 1}
    return cookie_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('name=Dima') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name') == {}
    assert parse_cookie(';') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima;Hello;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;Hello:age=28;') == {'name': 'Dima', 'Hello:age': '28'}
    assert parse_cookie('name=Dima=User;age=;') == {'name': 'Dima=User', 'age': ''}
