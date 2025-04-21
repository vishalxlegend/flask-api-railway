from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app running!"

@app.route("/run-code", methods=["POST"])
def run_code():
    code = request.json.get("code", "")
    try:
        exec_globals = {}
        exec(code, exec_globals)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        return jsonify({"image_base64": image_base64})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
