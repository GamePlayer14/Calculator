from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation')
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)

    if operation not in ["add", "subtract", "multiply", "divide"]:
        return jsonify({"error": "Invalid operation"}), 400

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = num1 / num2

    return jsonify({"operation": operation, "result": result})

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

# In[ ]:




