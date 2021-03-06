from flask import Flask, render_template, request
from qrcoderesponse import qrcoderesponse

app = Flask(__name__)

@app.route("/")
def show_form():
  return render_template('form.html')

@app.route("/qr")
def generate_qrcode():
  if request.method == "POST":
    text = request.form.get("text", None)
  else:
    text = request.args.get("text", None)

  if text is None:
    return "No text parameter", 400 #Bad Request

  return qrcoderesponse(text)
