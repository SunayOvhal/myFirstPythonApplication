from flask import Flask
app = Flask(__name__)
@app.route("/")
def main():
  return "Welcome!"
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
if __name__ == "__main__":
  app.run(host="0.0.0.0")
