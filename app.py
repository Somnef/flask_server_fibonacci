import flask
import random

app = flask.Flask(__name__)
random_id = random.randint(0, 1000)

# main route returns fibonacci number
@app.route('/<int:n>')
def fibonacci(n):
    return "Computer <" + str(random_id) + "> says Fibonacci number is: " + str(fib(n)) + "\n"

# fibonacci function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)