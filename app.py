from flask import Flask, render_template, request
from flask.ext.mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(
	DEBUG = True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'jobxposure@gmail.com',
	MAIL_PASSWORD = 'jobexposure'
	)

mail=Mail(app)


@app.route('/')
def index():
	return render_template('test.html')

@app.route('/video')
def video():
	return render_template('youtube.html')

@app.route('/send_video')
def send_video():
	msg = Message(
		'Hello',
		sender='jobxposure@gmail.com',
		recipients=['anirudh.c.mohan@gmail.com'])
	videoID = request.args.get('url',None)
	if videoID != None:
		url = "http://www.youtube.com/watch?v="+videoID
		msg.body = "This is the youtube link: " + url
		mail.send(msg)
		return "Sent"
	else:
		return "Video error"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)