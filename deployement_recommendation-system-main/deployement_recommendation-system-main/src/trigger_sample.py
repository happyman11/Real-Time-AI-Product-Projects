

from models import *
from jason_formatted import  *

#Text_input='Professional  Rust - Ultimate edition'
#This need to be extracted what user has putted in the text box or user has/had taken before
id=9
Text_input=id_title_mapping(id)

recommendation_models=Model()

#prediction=recommendation_models.pre_process_pipeline_prediction(Text_input)

recommended_course=format_output(recommendation_models.pre_process_pipeline_prediction(Text_input))
print(recommended_course)
