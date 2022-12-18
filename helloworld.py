from flask import Flask

app = Flask(__name__)
@app.route('/helloworld')

def helloworld():
    return "Hello , bhbjWelcome you will start creating your first CICD Pipeline"

if __name__ == "__main__":
    app.run(port=3000, debug=True)