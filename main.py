from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    query = text.upper()
    return render_template('results.html', query=query)

