from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!doctype html>
    <html><body style="font-family:system-ui, -apple-system, Segoe UI, Roboto, sans-serif; line-height:1.5; padding:2rem;">
      <p>Hey there,</p>
      <p>welcome to website deployed using a CI/CD pipeline.</p>
      <p>Thanks,<br>Sumit</p>
        <p>Thanks,<br>Sumit</p>
    </body></html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
