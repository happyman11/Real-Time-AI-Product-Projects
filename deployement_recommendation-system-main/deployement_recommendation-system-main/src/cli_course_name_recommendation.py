import argparse
from models import *
 

parser = argparse.ArgumentParser(description="Course Recommendation")
parser.add_argument("-o", "--Output", help = "Enter Course Name")
args = parser.parse_args()
 
if args.Output:
    print("Entered Course Name is: % s" % args.Output)





recommendation_models=Model()
prediction=recommendation_models.pre_process_pipeline_prediction(str(args.Output))

for i in range(0,len(prediction)):
    print(" Recommended Courses: ",prediction[i])

