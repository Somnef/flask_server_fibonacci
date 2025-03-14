import flask
import threading

app = flask.Flask(__name__)

# main route returns fibonacci number
@app.route('/<int:n>')
def fibonacci(n):
    # create a thread to calculate fibonacci number
    t = threading.Thread(target=fib, args=(n,))
    t.start()
    return f'Fibonacci number for {n} is being calculated in a separate thread'

# fibonacci function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)