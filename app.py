from flask import Flask, render_template
import psycopg2
conn = psycopg2.connect(dbname='albertastaduran', user='albertastaduran',
                        password='mypassword', host='localhost')
cursor = conn.cursor()
app = Flask(__name__)
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/')
def list_notebooks():
    cursor.execute('SELECT name, price FROM product')
    name_price = cursor.fetchall()
    name_price = sum(name_price,())
    name_price = list(name_price)
    name = []
    prices = []
    for value in name_price:
        if isint(value) :
            prices.append(value)
        else :
            name.append(value)
    for n, row in enumerate(name):
        name[n] = row.replace('\n','')
    return render_template('index.html', notebooks = name, prices = prices)
    conn.close()
@app.route('/notebook_pro_13')
def about_notebook_pro13():
    return 'pro13'
@app.route('/notebook_pro_15')
def about_notebook_pro15():
    return 'pro15'
@app.route('/notebook_air_13')
def about_notebook_air13():
    return 'air13'
@app.route('/notebook_12')
def about_notebook_12():
    return '12'
