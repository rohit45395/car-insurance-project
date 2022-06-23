from flask import Flask,render_template,request



app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('sample.html')

@app.route('/data',methods=['GET','POST'])
def info():
    var = request.form
    print(var)
    return render_template('result.html',Prediction=var)

if __name__=='__main__':
    app.run(debug=True)