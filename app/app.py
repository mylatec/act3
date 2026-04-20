from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():

   return jsonify({"message":"¡Hello from Flask in Docker. Version 4. This change will be displayed in 5 minutes more or less!"})

if __name__=="__main__":
   app.run(host="0.0.0.0", port=5000)
