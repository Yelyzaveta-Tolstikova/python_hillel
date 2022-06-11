def parse(url: str) -> dict:
    if url.find('?') == -1:
        return {}
    else:
        page, query = url.split('?')
        params_dict = {param[0]: param[1] for param in [pair.split('=') for pair in query.split('&')]
                       if len(param[0]) > 1 and len(param[1]) > 1}
        return params_dict


if __name__ == '__main__':
    assert parse('http://example.com/') == {}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name=') == {}
    assert parse('http://example.com/?&=purple&') == {}
    assert parse('http://example.com/?&color=purple&') == {'color': 'purple'}
    assert parse('http://example.com/?=') == {}
    assert parse('http://example.com/?&=&') == {}
