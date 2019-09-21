from flask import Flask, jsonify, request, abort

app = Flask(__name__)

about = {'about': 'Oliver Dragojević'}

portfolio_list = [
    {
        'id': 1,
        'godina': u'1994, 2003',
        'title': u'Cesarica, Trag u beskraju',
        'description': u'Porin za hit godine'
    },
    {
        'id': 2,
        'godina': u'1994, 2003',
        'title': u'Cesarica, Sve bi da za nju',        
        'description': u'Porin za pjesmu godine'
    },
	{
        'id': 3,
        'godina': u'1998',
        'title': u'Antologija',
        'description': u'Porin za najbolje reizdanje'
    },
	{
        'id': 4,
        'godina': u'2003, 2017, 2018',
        'title': u'Trag u beskraju, Gdje to piše?, Rusulica',
        'description': u'Porin za najbolju mušku vokalnu izvedbu'
    },
	{
        'id': 5,
        'godina': u'2006, 2014, 2017',
        'title': u'Vridilo je, Tišina mora, Familija',
        'description': u'Porin za album godine'
    },
	{
        'id': 6,
        'godina': u'2006',
        'title': u'Duša za nju',
        'description': u'Porin za najbolji aranžman'
    },
	{
        'id': 7,
        'godina': u'2006',
        'title': u'Vridilo je',
        'description': u'Porin za najbolju produkciju'
    },
	{
        'id': 8,
        'godina': u'2007',
        'title': u'A L"Olympia',
        'description': u'Porin za najbolji video program'
    },
	{
        'id': 9,
        'godina': u'2008, 2017, 2018',
        'title': u'Picaferaj, Ako voliš ovu ženu',
        'description': u'Porin za najbolju vokalnu suradnju'
    },
	{
        'id': 10,
        'godina': u'2014, 2017',
        'title': u'Tišina mora, Familija',
        'description': u'Porin za najbolji album pop glazbe'
    },
	{
        'id': 11,
        'godina': u'2018',
        'title': u'',
        'description': u'Porin za životno djelo'
    }   
]

contact = {'contact': 'Marko Jermen, mjermen@gmail.com'}

# (About) O meni 
@app.route('/api/v1/about', methods=['GET'])
def get_about():
    return jsonify(about)


# (Portfolio) Dohvat cijelog portfelja
@app.route('/api/v1/portfolio', methods=['GET'])
def get_portfolio():
    return jsonify(portfolio_list)

# (Contact) Kontakt
@app.route('/api/v1/contact', methods=['GET'])
def get_contact():
    return jsonify(contact)


if __name__ == '__main__':
    app.run(debug=True)