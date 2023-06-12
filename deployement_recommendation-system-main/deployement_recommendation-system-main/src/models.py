#import library


import joblib
import pandas as pd
from preprocessing import *







class Model:




    def __init__(self):

        self.model_path = "/home/happyman/Desktop/Projects]/deployement_recommendation-system/models/Tilte_recommendation_model.joblib"
        self.model = joblib.load(self.model_path)

        self.file_path = "/home/happyman/Desktop/Projects]/deployement_recommendation-system/Dataset/saved_dataset_with_cluster/datasetwithcluster.csv"



    def prediction(self, sentence):

        return self.model.predict(sentence)


    def select_dataset(self,prediction):

        #print("select_dataset")
        course_dataset=pd.read_csv(self.file_path)
        selected_course=[]


        for i,labels in enumerate(course_dataset['cluster']):

            if labels == prediction:

                selected_course.append(i)

        course_names=[]

        for i in range(0,len(selected_course)):

            course_names.append(course_dataset["Title"][i])


        #print("select_datasetend")
        return(course_names)



    def pre_process_pipeline_prediction(self,text):

        santization_obj=sanitisationtext()

        lower_cased=santization_obj.remove_punctuation(text)

        tokenised_text=santization_obj.tokenise_Sentence(lower_cased)

        no_stop_words=santization_obj.remove_stop_words(tokenised_text)

        sanitised_text=santization_obj.remove_spaces(no_stop_words)

        embedding_text=santization_obj.load_embedding()

        vec_text= santization_obj.word_embedding(sanitised_text,embedding_text)

        feature_text=santization_obj.padding(vec_text)

        np_array_feature_text=np.asarray(feature_text)


        features_text_input=np_array_feature_text.reshape(-1, 10)

        prediction=self.prediction(features_text_input)

        recommended_courses_names=self.select_dataset(prediction)

        return(recommended_courses_names)
