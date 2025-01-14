from flask import Flask , render_template , send_file 

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/services',methods=['GET'])
def services():
    return render_template('services.html')

@app.route('/user/app',methods=['GET'])
def user_app():
    return render_template('user_app.html')

@app.route('/user/portal',methods=['GET'])
def user_portal():
    return render_template('user_portal.html')

@app.route('/user/download_app', methods=['GET'])
def download_app():
    return send_file('static/Fortify.apk', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')