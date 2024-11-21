from flask import Flask, render_template


app = Flask(__name__,static_folder='build', static_url_path='/')

@app.route('/')
def index():    
    return app.send_static_file('index.html')

@app.route('/name')
def name():
    return 'Bob Ozeranski'

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')