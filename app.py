from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

    return f'''
    <html>
    <head>
        <title>POC-3 Interactive Calculator</title>

        <style>

            body {{
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                font-family: Arial, sans-serif;
                color: white;
                text-align: center;
                padding-top: 40px;
            }}

            .container {{
                width: 60%;
                margin: auto;
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            }}

            h1 {{
                color: #00ffcc;
                font-size: 45px;
            }}

            h2 {{
                color: #ffd700;
            }}

            input, select {{
                padding: 12px;
                width: 200px;
                margin: 10px;
                border-radius: 10px;
                border: none;
                font-size: 16px;
            }}

            button {{
                background: #00ffcc;
                color: black;
                padding: 12px 25px;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                cursor: pointer;
                margin-top: 15px;
            }}

            button:hover {{
                background: #00ccaa;
            }}

            .result {{
                margin-top: 25px;
                font-size: 30px;
                color: #ffeb3b;
            }}


        </style>
    </head>

    <body>

        <div class="container">

            <h1>POC-3</h1>

            <h2>Interactive Python Calculator </h2>

            <form method="POST">

                <input type="number" step="any" name="num1" placeholder="Enter First Number" required>

                <br>

                <input type="number" step="any" name="num2" placeholder="Enter Second Number" required>

                <br>

                <select name="operation">

                    <option value="add">Addition (+)</option>
                    <option value="subtract">Subtraction (-)</option>
                    <option value="multiply">Multiplication (*)</option>
                    <option value="divide">Division (/)</option>

                </select>

                <br>

                <button type="submit">Calculate</button>

            </form>

            <div class="result">
                Result: {result}
            </div>



    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
