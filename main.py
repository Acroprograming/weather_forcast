from flask import Flask ,render_template,request
import pandas as pd 
import ast
app = Flask(__name__)


@app.route("/")
@app.route("/home",endpoint="index")
def home():
	return render_template("basic.html")


@app.route("/test_data",endpoint="test_data")
def test_data():
	df = pd.DataFrame([['a', 'b'], ['c', 'd']],index=[0,1],columns=['col 1', 'col 2'])
	data=df.to_json(orient='index')
	data=ast.literal_eval(data)
	print(data)
	return render_template("test_data.html",data=data)

@app.route("/result",endpoint="result",methods=['GET', 'POST'])
def result():
	i=request.form['index']
	i=int(i)
	#print("hiiiiiiiiii  "+i)
	i=int(i)
	df = pd.DataFrame([['a', 'b'], ['c', 'd']],index=[0,1],columns=['col 1', 'col 2'])
	s=str(pd.DataFrame(df.iloc[i]).to_html())
	return s

if __name__ == '__main__':
    app.run(debug=True)