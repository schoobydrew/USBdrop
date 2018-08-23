from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['GET', 'POST']) #allow POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        username = request.form.get('username')
        company = request.form.get('company')
        time = request.form.get('time')
        print username, company, time
        logs = open("{}.csv".format(company), 'a+')
        print >> logs, "{},{},{}".format(time, username, company)
        logs.close()

    return '''<form method="POST"> <h1>UP</h1>
              </form>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
