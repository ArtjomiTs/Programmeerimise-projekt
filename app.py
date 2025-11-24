'''
Projekt:
Interaktiivne ÕIS-i kasutamist toetav rakendus veebilehe kujul.

Töö autorid:
Mihkel Tomson
Artjom Tšerkassov

Juhend:
Programmi käivitamiseks "python app.py"
Veebilehele on hetkel lisatud tagasiside funktsionaalsus, teised funktsioonid lisanduvad
järgneva töö käigus. 

'''



from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# /// Avaleht (avaleht.html)
@app.route('/')
def avaleht():
    return render_template('avaleht.html')

# /// Tagasiside leht (tagasiside.html)
@app.route('/tagasiside', methods=['GET', 'POST'])
def tagasiside():
    if request.method == 'POST':
        feedback_message = request.form['feedback']
        print('Kasutaja tagasiside:', feedback_message)
        return redirect(url_for('aitah'))
    return render_template('tagasiside.html')

# /// Tänuleht
@app.route('/aitah')
def aitah():
    return '<h2>Aitäh tagasiside eest!</h2><a href="/">Tagasi avalehele</a>'

# /// profiili leht (profiil.html)
@app.route ('/profiil')
def profiil():
    return render_template('profiil.html')

# /// Postkasti leht (postkast.html)
@app.route ('/postkast')
def postkast():
    return render_template('postkast.html')

# /// Algne chatbot funktsioon
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "tere" in user_input or "hello" in user_input:
        return "Tere! Kuidas saan aidata?"
    elif "aitäh" in user_input:
        return "Pole tänu väärt!"
    else:
        return "Vabandust, ma ei saa sellest aru. Proovi teist küsimust."
    
# /// Chatboti leht
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# /// API vastus kasutaja sõnumile
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['message']
    response = chatbot_response(user_input)
    return jsonify({'response' : response})

if __name__ == '__main__':
    app.run(debug=True)
