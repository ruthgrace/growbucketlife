from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/instructable')
def instructable():
    return redirect("https://www.instructables.com/id/Grow-Anything-Grow-Bucket-for-50/", code=302)
