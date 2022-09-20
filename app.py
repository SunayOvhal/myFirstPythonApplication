from flask import Flask
from flask import request, redirect
import requests
app = Flask(__name__)
@app.route("/")
def main():
  return "Welcome!"
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
@app.route('/postMethod',methods = ['POST', 'GET'])
def postMethod():
   if request.method == 'POST':
      user = request.form['nm']
      return 'postcall'
# return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
if __name__ == "__main__":
  app.run(host="0.0.0.0")
