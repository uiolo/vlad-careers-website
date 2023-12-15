from flask import Flask, render_template

app = Flask(__name__)

jobs = [{
    "job_name": "Software Engineer",
    "salary": 100000,
    "location": "San Francisco"
}, {
    "job_name": "Data Scientist",
    "salary": 95000,
    "location": "New York"
}, {
    "job_name": "Product Manager",
    "salary": 190000,
    "location": "Seattle"
}]


@app.route('/')
def hello_page():
  return render_template('home.html', jobs=jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
