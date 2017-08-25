from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route('/health')
def index():
    return 'hello world'

@app.route('/test', methods=['POST'])
def test():
    call = request.form['call']
    param = eval(request.form['param'])
    rule = request.form['rule']
    return test1(rule, param, call)

def test1(rule,params, call):
    try:
        exec (rule)
        for param in params.items():
            print type_check(param[1])
            assignment = u"{}={}".format(param[0], type_check(param[1]))
            exec assignment
        print eval(call)
        result = {"response_code": '00', 'content': eval(call)}
        return jsonify(result)
    except BaseException, data:
        return data

def type_check(value):
    try:
        if value == unicode(value):
            return value
        else:
            return value
    except BaseException:
        return '\'' + value.decode('utf-8') + '\''


if __name__ == '__main__':
    app.run(debug=True, port=8899, host='0.0.0.0')