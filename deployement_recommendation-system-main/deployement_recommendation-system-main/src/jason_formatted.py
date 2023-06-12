import os
from dotenv import load_dotenv
import json
from urllib.request import urlopen

def id_title_mapping(courseid):

    load_dotenv()
    response = urlopen(os.getenv('LINK_JSON'))
    course_data_json = json.loads(response.read())

    for i in range(0,int(course_data_json['count'])):

        if courseid  == course_data_json['data'][i]['id']:
             return(course_data_json['data'][i]['title'])



def format_output(Recommended_courses):


    load_dotenv()
    response = urlopen(os.getenv('LINK_JSON'))
    course_data_json = json.loads(response.read())

    recommended_course={}
    recommended_course["provided_by"]="Maggana API services"
    recommended_course["count"]=len(Recommended_courses)-1
    for recommendation in Recommended_courses:


        for i in range(0,int(course_data_json['count'])):

            if recommendation  == course_data_json['data'][i]['title']:
                course_info={}

                course_id=course_data_json['data'][i]['id']
                course_title=course_data_json['data'][i]['title']
                course_instructor=course_data_json['data'][i]['instructor']
                course_price=course_data_json['data'][i]['price']
                course_level=course_data_json['data'][i]['level']

                print("course_id ->>",course_id)
                print("course_Title ->>",course_title)
                print("course_instructor ->>", course_instructor)
                print("course_price ->>", course_price)
                print("course_level ->>", course_level)

                #add if else conditions
                course_info['id']=course_id
                course_info['Title']=course_title
                course_info["instructor"]=course_instructor
                course_info["level"]=course_level
                course_info["price"]=course_price


                name="Recommended Courses : "+str(i)
                recommended_course[name]=[course_info]

                #print(json.dumps(recommended_course))

    return(json.dumps(recommended_course))

# SAMPLE_DATA=["R/Bioconductor for Bioinfomatics","Rust up and Running"]
# print(format_output(SAMPLE_DATA))
id=9
print(id_title_mapping(id))
