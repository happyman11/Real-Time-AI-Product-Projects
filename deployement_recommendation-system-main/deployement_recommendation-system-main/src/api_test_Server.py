from flask import Flask,request,jsonify




app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask Api --- Course Recommendation System'

@app.route('/course_recommendation', methods=['POST'])
def post_method():
    input_json = request.get_json(force=True) 
    print(input_json)
    return jsonify("Received")
    

if __name__ == '__main__':
    app.run(debug=True)