from flask import Flask
from flask import render_template
from flask import Response
import cv2

app = Flask(__name__)


url = 'https://cctvatis4.ntpc.gov.tw/C000267'

def stream1():
    cap = cv2.VideoCapture(url)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()

            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def stream2():
    cap = cv2.VideoCapture(url)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, buffer = cv2.imencode(".jpg", gray)
            frame = buffer.tobytes()

            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




@app.route("/")
def home():
    return render_template("home.html")




@app.route('/video_feed1')
def video_feed1():
    return Response(stream1(), mimetype = 'multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2')
def video_feed2():
    return Response(stream2(), mimetype = 'multipart/x-mixed-replace; boundary=frame')




if __name__ == "__main__":
    app.run()

# git init
# heroku git:remote -a family-project-website

# git add .
# git commit -m "First Deploy"
# git push heroku master
