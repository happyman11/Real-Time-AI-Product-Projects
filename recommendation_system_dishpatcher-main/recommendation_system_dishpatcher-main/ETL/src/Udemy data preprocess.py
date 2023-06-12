import numpy as np

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf,lower
from pyspark.sql.types import StringType,IntegerType,FloatType,LongType,BooleanType,TimestampType
from pyspark.sql.types import StructType
spark = SparkSession.builder\
        .master("local")\
        .appName("RECOMMENDATION SYSTEM")\
        .config('spark.ui.port', '4050')\
        .getOrCreate()


schema = StructType() \
      .add("Course_ID",IntegerType(),True) \
      .add("Course Title",StringType(),True) \
      .add("Url",StringType(),True) \
      .add("Is_paid",BooleanType(),True) \
      .add("Price",IntegerType(),True) \
      .add("Num Subscriber",IntegerType(),True) \
      .add("Num Reviewers",IntegerType(),True) \
      .add("Num Lectures",IntegerType(),True) \
      .add("Level",StringType(),True) \
      .add("Content Duration",FloatType(),True) \
      .add("Publish Timestamp",TimestampType(),True) \
      .add("Subjects",StringType(),True) 
      
df_with_schema = spark.read.format("csv") \
      .option("header", True) \
      .schema(schema) \
      .load("/home/transi/Desktop/Recommendation System/ETL/src/glove_files/glove.6B/glove.6B.50d.txt")


df_with_schema.show()

df_Course_Title=df_with_schema.select(col("Course Title"))
df_Course_Sector=df_with_schema.select(col("Subjects"))

from pyspark.sql.functions import udf

import string
regular_punct = list(string.punctuation)
extra_punct = [
    ',', '.', '"', ':', ')', '(', '!', '?', '|', ';', "'", '$', '&',
    '/', '[', ']', '>', '%', '=', '#', '*', '+', '\\', '•',  '~', '@', '£',
    '·', '_', '{', '}', '©', '^', '®', '`',  '<', '→', '°', '€', '™', '›',
    '♥', '←', '×', '§', '″', '′', 'Â', '█', '½', 'à', '…', '“', '★', '”',
    '–', '●', 'â', '►', '−', '¢', '²', '¬', '░', '¶', '↑', '±', '¿', '▾',
    '═', '¦', '║', '―', '¥', '▓', '—', '‹', '─', '▒', '：', '¼', '⊕', '▼',
    '▪', '†', '■', '’', '▀', '¨', '▄', '♫', '☆', 'é', '¯', '♦', '¤', '▲',
    'è', '¸', '¾', 'Ã', '⋅', '‘', '∞', '∙', '）', '↓', '、', '│', '（', '»',
    '，', '♪', '╩', '╚', '³', '・', '╦', '╣', '╔', '╗', '▬', '❤', 'ï', 'Ø',
    '¹', '≤', '‡', '√', '«', '»', '´', 'º', '¾', '¡', '§', '£', '₤','⌨','☝']

all_punct = list(set(regular_punct + extra_punct))

def remove_punctuation(text):
    for punc in all_punct:
        if punc in text:
            text = text.replace(punc, ' ')
    return (text.strip().lower())
    

DF_string_remover = udf(lambda m: remove_punctuation(m))

df_Course_Title=df_Course_Title.withColumn("Course Title",DF_string_remover("Course Title"))
df_Course_Sector=df_Course_Sector.withColumn("Subjects",DF_string_remover("Subjects"))
