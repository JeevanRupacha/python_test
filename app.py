from flask import Flask, render_template, request
import os
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def printing():
    return "test print"

@app.route('/<string:path>')
def html_render(path):
    return render_template(path)

@app.route('/submit_from', methods=['POST','GET'])
def submit_from():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_db(data)
        csv_write(data)
        return data
    else:
        return "something wrong to open file"

def write_db(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        password = data["password"]
        database.seek(0,os.SEEK_END)
        database.write(f'\n{email}, {password}')

def csv_write(data):
    with open('database.csv', mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file,delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)
        email = data["email"]
        password = data["password"]
        csv_writer.writerow([email,password])


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)

        