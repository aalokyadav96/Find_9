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
    query = text.lower()
    users = [ 
        ["Blockchain - Wikipedia ","https://en.wikipedia.org/wiki/Blockchain_(database)","A blockchain, originally block chain, is a continuously growing list of records, called blocks, which are linked and secured using cryptography. Each block typically contains a cryptographic hash of the previous block, a timestamp and transaction data."],
        ["Blockchain", "https://www.blockchain.com","Blockchain is the world's leading software platform for digital assets. Offering the largest production block chain platform in the world, we are using new technology to build a radically better financial system."],
        ["What is Blockchain? | Fortune", "fortune.com/2016/05/23/blockchain-definition/", "Though it sounds like a series of defensive maneuvers ripped out of an NFL playbook, the blockchain is actually a way to structure data, and the foundation of cryptocurrencies like Bitcoin."] ]
    if query == '':
        return render_template('form.html')
    else:
        return render_template('results.html', query=query, results=users)

