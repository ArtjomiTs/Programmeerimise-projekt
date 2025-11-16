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



from flask import Flask, render_template, request, redirect, url_for

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
@app.route ('/postkast.html')
def postkast():
    return render_template('postkast.html')

if __name__ == '__main__':
    app.run(debug=True)
