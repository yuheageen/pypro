import  socket
host = "203.250.133.88"
port = 11954
Buffer_SIZE = 128

from Flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()