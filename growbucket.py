import logging
import stripe
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, redirect, request, send_from_directory
from config import testkey, prodkey, testsecretkey, prodsecretkey

KEY = prodkey
SECRET = prodsecretkey
QUANTITIES = [1, 2, 3, 4, 5]

app = Flask(__name__)
handler = RotatingFileHandler('/var/log/growbucket/app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

def get_numbers(quantity, cost):
    numbers = {}
    numbers['quantity'] = quantity
    numbers['cost'] = cost * numbers['quantity']
    numbers['taxtotalcents'] = (85 * numbers['cost']) / 10
    numbers['taxcents'] = numbers['taxtotalcents'] % 100
    numbers['taxdollars'] = numbers['taxtotalcents'] / 100
    numbers['totalcents'] = numbers['taxcents']
    numbers['totaldollars'] = numbers['taxdollars'] + numbers['cost']
    numbers['stripetotal'] = numbers['totaldollars'] * 100 + numbers['totalcents']
    return numbers

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq')
@app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route('/documents')
@app.route('/documents.html')
def documents():
    return render_template('documents.html')

@app.route('/payment', methods = ['GET', 'POST'])
def payment():
    if request.method == 'GET':
        numbers = get_numbers(1, 50)
        return render_template('payment.html',
                               key=KEY,
                               quantities=QUANTITIES,
                               quantity=numbers['quantity'],
                               cost=numbers['cost'],
                               taxcents=numbers['taxcents'],
                               taxdollars=numbers['taxdollars'],
                               totalcents=numbers['totalcents'],
                               totaldollars=numbers['totaldollars'],
                               stripetotal=numbers['stripetotal'])
    if request.method == 'POST':
        numbers = get_numbers(int(request.form.get('quantity')), 50)
        return render_template('payment.html',
                               key=KEY,
                               quantities=QUANTITIES,
                               quantity=numbers['quantity'],
                               cost=numbers['cost'],
                               taxcents=numbers['taxcents'],
                               taxdollars=numbers['taxdollars'],
                               totalcents=numbers['totalcents'],
                               totaldollars=numbers['totaldollars'],
                               stripetotal=numbers['stripetotal'])

@app.route('/two', methods = ['GET', 'POST'])
def two_dollars():
    if request.method == 'GET':
        numbers = get_numbers(1, 2)
        return render_template('two.html',
                               key=KEY,
                               quantities=QUANTITIES,
                               quantity=numbers['quantity'],
                               cost=numbers['cost'],
                               taxcents=numbers['taxcents'],
                               taxdollars=numbers['taxdollars'],
                               totalcents=numbers['totalcents'],
                               totaldollars=numbers['totaldollars'],
                               stripetotal=numbers['stripetotal'])
    if request.method == 'POST':
        numbers = get_numbers(int(request.form.get('quantity')), 2)
        return render_template('two.html',
                               key=KEY,
                               quantities=QUANTITIES,
                               quantity=numbers['quantity'],
                               cost=numbers['cost'],
                               taxcents=numbers['taxcents'],
                               taxdollars=numbers['taxdollars'],
                               totalcents=numbers['totalcents'],
                               totaldollars=numbers['totaldollars'],
                               stripetotal=numbers['stripetotal'])

@app.route('/ten', methods = ['GET', 'POST'])
def ten_dollars():
    if request.method == 'GET':
        numbers = get_numbers(1, 10)
        return render_template('ten.html',
                               key=KEY,
                               quantities=QUANTITIES,
                               quantity=numbers['quantity'],
                               cost=numbers['cost'],
                               taxcents=numbers['taxcents'],
                               taxdollars=numbers['taxdollars'],
                               totalcents=numbers['totalcents'],
                               totaldollars=numbers['totaldollars'],
                               stripetotal=numbers['stripetotal'])
    if request.method == 'POST':
        numbers = get_numbers(int(request.form.get('quantity')), 10)
        return render_template('ten.html',
                               key=KEY,
                               quantities=QUANTITIES,
                               quantity=numbers['quantity'],
                               cost=numbers['cost'],
                               taxcents=numbers['taxcents'],
                               taxdollars=numbers['taxdollars'],
                               totalcents=numbers['totalcents'],
                               totaldollars=numbers['totaldollars'],
                               stripetotal=numbers['stripetotal'])

@app.route('/checkout', methods = ['POST'])
def checkout():
    token = request.form.get('stripeToken')
    amount = request.form.get('stripetotal')
    stripe.api_key = SECRET
    charge = stripe.Charge.create(
      amount=str(amount),
      description="Grow Bucket Kit",
      currency="usd",
      receipt_email=request.form.get('stripeEmail'),
      source=token
    )
    return render_template('checkout.html')

@app.route('/donate', methods = ['POST'])
def donate():
    token = request.form.get('stripeToken')
    amount = request.form.get('stripetotal')
    stripe.api_key = SECRET
    charge = stripe.Charge.create(
      amount=str(amount),
      description="Grow Bucket Donation",
      currency="usd",
      receipt_email=request.form.get('stripeEmail'),
      source=token
    )
    return render_template('donate.html')

@app.route('/instructable')
@app.route('/instructable.html')
def instructable():
    return redirect("https://www.instructables.com/id/Grow-Anything-Grow-Bucket-for-50/", code=302)
