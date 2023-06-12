from flask import Flask,request,jsonify
from models import *
 



app = Flask(__name__)


@app.route('/')
def hello_world():
    return """Flask Api --- Course Recommendation System \n
              Post method: /course_recommendation
                  """

@app.route('/course_recommendation', methods=['POST'])
def post_method():
    
    
    input_json = request.get_json(force=True) 
    print(input_json['Course Name'])
    recommendation_models=Model()
    prediction=recommendation_models.pre_process_pipeline_prediction(str(input_json['Course Name']))
    
   
    
    return jsonify(prediction)
    

if __name__ == '__main__':
    app.run(debug=True)