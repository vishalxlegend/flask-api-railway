from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask app is running!"

@app.route('/generate_plot', methods=['POST'])
def generate_plot():
    data = request.get_json()
    code = data.get('code')

    try:
        local_vars = {}
        exec(code, {'plt': plt, 'io': io, 'base64': base64}, local_vars)
        img_base64 = local_vars['img_base64']
        return jsonify({"image_base64": img_base64})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
