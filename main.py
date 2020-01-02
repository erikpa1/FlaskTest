from flask import Flask

app = Flask(__name__);

@app.route('/')
def dada():
    return "Hello World";


if __name__ == '__main__':
   app.run();

#app.debug = True
#app.run()
#app.run(debug = True)

#@app.route('/hello/<name>')
#def hello_name(name):
#  return 'Hello %s!' % name