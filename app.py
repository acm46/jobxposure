from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	return render_template('test.html')

@app.route('/video')
def video():
	return render_template('youtube.html')

if __name__ == '__main__':
    app.run()