from flask import Flask, render_template
#Create instance of app
app = Flask(__name__)

num_clicks = 0

# Default endpoint
@app.route('/')
def index():
    print(num_clicks)
    return render_template('index.html', num_clicks=num_clicks)

# click post api
@app.route('/click', methods=['POST'])
def click():
    global num_clicks
    num_clicks += 1
    return f"I was clicked"
