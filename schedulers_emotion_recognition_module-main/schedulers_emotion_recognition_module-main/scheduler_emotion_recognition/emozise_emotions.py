from emoji import emojize




def emojiemotion(labels):

    emojis=[]
    for i in labels:
        if i =="Happy":
            emojis.append(":rolling_on_the_floor_laughing:")
        elif i == "Angry":
            emojis.append(":pouting_face:")
        elif i == "Disgust":
            emojis.append(":disguised_face:")
        elif i == "Fear":
            emojis.append(":fearful_face:")
        elif i == "Sad":
            emojis.append(":sad_but_relieved_face:")
        elif i == "Surprise":
            emojis.append(":astonished_face:")
        elif i == "Neutral":
           emojis.append(":neutral_face:")

    return(emojis)
