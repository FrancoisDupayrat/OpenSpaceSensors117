from flask import Flask, render_template
import main
app = Flask(__name__)

values = main.getValues()

@app.context_processor
def get_legacy_var():
    return dict(get_legacy_var=main.getValues())

@app.route('/')
def index():
    return render_template('index.html', values=values)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
