import openai
import pandas as pd
import deepl
import pyttsx3
import time
import os
import azure.cognitiveservices.speech as speechsdk
import time
import csv




def listen(language):
    speech_config.speech_recognition_language=language
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))

        return speech_recognition_result.text
    

def speak(input,voice):
    
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_config.speech_synthesis_voice_name=voice
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_text_async(input).get()
    if speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Azure Speech synthesis canceled: {}".format(cancellation_details.reason))
       
        engine = pyttsx3.init()
        engine.setProperty('voice', voice)
        engine.say(input)
        engine.runAndWait()
        print("stop")
    
    return True


def to_english(text,language):
    if language=="EN":
        return text
    result = translator.translate_text(text,source_lang=language,target_lang="EN-GB")
    #result=translator.translate(text, dest="en")
    return result.text

def english_to(text,language):
    if language=="EN":
        return text
    result = translator.translate_text(text,target_lang=language)
    #result=translator.translate(text, dest=language.lower())
    return result.text


def chat(question,chat_log = None):
    t_chat=time.time()
    prompt = f"{chat_log}Human: {question}\nAI-Doctor:"

    try:
        response = openai.Completion.create(
            prompt = prompt,
            engine="text-davinci-003",
            #engine="text-curie-001",
            temperature = 0.75,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.7,
            max_tokens=150,
            stop = ["Human:","http","AI","Regards"])
        t_chat_1=time.time()
        print("openai_request:", t_chat_1-t_chat)
    
        return (prompt,response.choices[0].text)

    except:

        return False
        
        
    

def classification(answer,prompt):

    response = openai.Completion.create(
        model="text-davinci-001",
        prompt=prompt+"\nAnswer: \""+answer+"\"\n\ncategory:",
        temperature=0,
        max_tokens=10,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
)
    return (response.choices[0].text)

def classification_prompt_generator(answer,question_list):

    question = question_list[0]

    if question_list[3]== None and question_list[4]== None:
        answers = "\""+question_list[1]+"\" or \""+question_list[2]+"\""
    elif question_list[3]!= None and question_list[4]== None:
        answers = "\""+'", "'.join(question_list[1:3])+"\" or \""+question_list[3]+"\""
    else:
        answers = "\""+'", "'.join(question_list[1:4])+"\" or \""+question_list[4]+"\""

    example1="\nAnswer: \""+question_list[5]+"\"\n\ncategory: "+question_list[6]
    example2="\nAnswer: \""+question_list[7]+"\"\n\ncategory: "+question_list[8]
    example3="\nAnswer: \""+question_list[9]+"\"\n\ncategory: "+question_list[10]

    classification_prompt = "Decide whether a patients answer to a doctors question: \""+question+"\" can be mapped to one of the four categories: "+answers+".\n\n"+example1+"\n\n"+example2+"\n\n"+example3

    classification_prompt= classification_prompt+"\nAnswer: \""+answer+"\"\n\ncategory:"

    return classification_prompt

def get_topic(answer):

    topic_prompt = "Determine the primary reason why a patient is seeking medical attention by analyzing their response to the question: 'What brings you in to see the doctor today?'\nYour analysis should focus on extracting the main complaint or symptoms that the patient is experiencing. Examples of possible reasons for their visit may include: 'chest pain', 'difficulty breathing', 'abdominal pain', 'skin rash', 'headache' or similar topics. In three tokens or less. \n\nPatient-response: I have severe headace since yesterday.\nTopic: Headache\n\nPatient response: My joints are feeling incredibly sensitive, allmost painful.\nTopic: Joint pain\n\nPatient response: I have severe headache since yesterday.\nTopic: Headache\n\nPatient response: I have been experiencing shortness of breath for the past few days.\nTopic: Difficulty Breathing\n\nPatient response: I have been experiencing stomach cramps and nausea.\nTopic: Abdominal pain\n\nPatient response: I have a rash all over my body.\nTopic: Skin rash"

    topic_prompt= topic_prompt+"\n\nPatient-response: \""+answer+"\"\n\Topic:"

    return topic_prompt


def certainty_prompt_generator(answer,question):

    certainty_prompt="Decide weather the patient knows or doesn't know the answer to the question: \""+question+"\" \n\nAnswer: \"I am not sure about this.\"\nCategory: I don't know\n\nAnswer: \"I can not tell you exactly.\"\nCategory: I don't know\n\nAnswer: \"The pain worsens slightly.\"\nCategory: I know\n\nAnswer: \"Yes, i vomited a lot.\"\nCategory: I know\n\nAnswer: \"Well i am not really certain. It just came over time.\"\nCategory: I don't know\n\nAnswer: \"Since three days, however i can not recall if it started in the evenening or around noon.\"\nCategory: I know"

    certainty_prompt= certainty_prompt+"\nAnswer: \""+answer+"\"\n\nCategory:"

    return certainty_prompt

def further_details_prompt_generator(answer,question):

    further_details_prompt="Decide weather the patient wants to know further details on the question: \""+question+"\" by asking something about the questions intent.\n\nAnswer: \"I am not sure, can you please tell me more about this?\"\nCategory: Uncertain answer\n\nAnswer: Eating affects my pain in a worse way.\nCategory: Certain answer\n\nAnswer: Why would you need to know this?\nCategory: Uncertain answer\n\nAnswer: The symptoms get stronger.\nCategory: Certain answer\n\nAnswer: I do not get why this is relevant for me.\nCategory: Uncertain answer"

    further_details_prompt= further_details_prompt+"\nAnswer: \""+answer+"\"\n\nCategory:"

    return further_details_prompt

def generate_information(answer,question):

    answer=answer.replace(".", "")

    answer=answer+".\nInformation: Combine the patients answer and the following question: \""+question+ "\""+"into one sentence reffering to the patient in an empathic manner and asking suggestive"

    answer=answer+".\nInformation: Combine the patients answer and the following question: \""+question+ "\""+"into one sentence reffering to the patient in an empathic manner and asking suggestive"


    return answer

def rephrase_question(answer,question):

    answer=answer.replace(".", "")

    rephrased_question=answer+".\nInformation: The patient is uncertain. Ask the patient again in a different manner, refferencing his uncertainty, about the question: \""+question+ "\""

    return rephrased_question

def give_further_details(answer,question):

    answer=answer.replace(".", "")

    rephrased_question=answer+".\nInformation: Ask the prior question: \""+question+ "\"again in a polite and empathic manner, explaining long and in detail its relevace to the diagnosis of abdominal pain lengthy and in detail reffering to the patients question."

    return rephrased_question

def connection_error(language,language_voice_id):
    speak(english_to("The server is currently unavailable, please try again shortly",language),language_voice_id)
    english_to("The server is currently unavailable, please try again shortly",language)

def main(language,attribute):

    print(language)

    global speech_config
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

    global translator
    translator = deepl.Translator(os.environ.get("DEEPL_API_KEY"))

    openai.api_key = os.environ.get('OPENAI_API_KEY')
    

    if attribute.lower() == "doctor":

        start_chat_log ="""The following is a conversation with an AI doctor. The doctor is empathetic, helpfull, respectfull, and nice.\nHuman: Hello, who are you?\nAI-Doctor: I am a virtual doctor with a lot of knowlede in the medical domain. I am able to help you regarding medical questions. How can I help you today?\n"""

        greeting="\nHi, i am a virtual doctor. Just speak in any language you want to me. Please give me time to respond after finishing with your input. To stop the conversation just say \"stop\". How can i help you today?"
    elif attribute.lower() =="anything":

        start_chat_log ="""The following is a conversation with an AI. The AI is freindly, helpfull, intelligent, and nice. It gives lengthy and elaborate answers to humans talking with it.\nHuman: Hello, who are you?\nAI: I am a virtual Chatbot with a lot of knowlede in different domains. I am able to talk about different topics and intereests. What do you want to talk about today?\n"""

        greeting="\nHi, i am a general chatbot. Just speak in any language you want to me. Please give me time to respond after finishing with your input. To stop the conversation just say \"stop\". How can i help you today?"

    answer = ""

    log=[]

    df = pd.read_csv('azure_voices.csv', sep=';')
    language_country_id=df[df['language_country'].str.contains(language.lower())].iloc[0]["language_country"]
    language_voice_id=df[df['language_country'].str.contains(language.lower())].iloc[0]["id"]

    speak(english_to(greeting,language),language_voice_id)

    feedback=listen(language_country_id)

    answer=to_english(feedback,language)

    log += [answer]

    #df = pd.read_csv('mac_voices.csv', sep=';')
    
    print(english_to("Answer",language)+feedback)

    topic_prompt=get_topic(answer)
    topic=classification(answer,topic_prompt)
    #print(english_to("AI-Doctor: You selected help for: "+topic,language))


    while "abdominal" not in topic.lower() and "stop" not in feedback.lower():

        print(feedback.lower())

        x=chat(answer,start_chat_log)

        if x== False:
            connection_error(language,language_country_id)

        log += [x[1].lstrip()]

        #print(english_to("AI-Doctor:"+x[1].lstrip(),language))

        speak(english_to(x[1].lstrip(),language),language_voice_id)


        start_chat_log=x[0]+x[1]

        #answer= to_english(input("Human: ")
        feedback=listen(language_country_id)
        while feedback == None:
            speak(english_to("Sorry, i did not understand you, could you please repeat that?",language),language_voice_id)
            feedback=listen(language_country_id)

        answer=to_english(feedback,language)
        log += [answer]
        topic_prompt=get_topic(answer)
        topic=classification(answer,topic_prompt)


    while "stop" not in feedback.lower():

        speak(english_to("You selected help for:"+topic,language),language_voice_id)
        print(topic)

        df = pd.read_csv('QA_abdominal_pain.csv', sep=';')

        for index, row in df.iterrows():

            #neue farge, antwortmöglichkeiten bekommen
            question=row.values.flatten().tolist()

            #aktuelle antwort und neue frage zusammen in einen prompt schreiben und als information übergeben
            answer=generate_information(answer,question[0])

            x=chat(answer,start_chat_log)
            if x== False:
                connection_error(language,language_country_id)
            log += [x[1].lstrip()]
            print(english_to("AI-Doctor:"+x[1].lstrip(),language))
            speak(english_to(x[1].lstrip(),language),language_voice_id)
            start_chat_log=x[0]+x[1].lstrip()

            #answer= to_english(input("Human: "))
            feedback=listen(language_country_id)
            while feedback == None:
                speak(english_to("Sorry, i did not understand you, could you please repeat that?",language),language_voice_id)
                feedback=listen(language_country_id)
            answer=to_english(feedback,language)
            log += [answer]

            certainty_prompt=certainty_prompt_generator(answer,question[0])
            certainty_answer=classification(answer,certainty_prompt)

            further_details_prompt=further_details_prompt_generator(answer,question[0])
            further_details_answer=classification(answer,certainty_prompt)

            if "I don't know" in certainty_answer or "What does this mean" in further_details_answer:
                if "I don't know" in certainty_answer:
                    answer=rephrase_question(answer,question[0])
                elif "What does this mean" in further_details_answer:
                    answer=give_further_details(answer,question[0])

                x=chat(answer,start_chat_log)
                if x== False:
                    connection_error(language,language_country_id)
                log += [x[1].lstrip()]
                print(english_to("AI-Doctor:"+x[1].lstrip(),language))
                speak(english_to(x[1].lstrip(),language),language_voice_id)
                start_chat_log=x[0]+x[1].lstrip()
                #answer= to_english(input("Human: "))
                feedback=listen(language_country_id)
                while feedback == None:
                    speak(english_to("Sorry, i did not understand you, could you please repeat that?",language),language_voice_id)
                    feedback=listen(language_country_id)
                answer=to_english(feedback,language)
                log += [answer]

            #antwort als prompt verpacken
            classification_prompt=classification_prompt_generator(answer,question)

            #prompt GPT-3 zur klassifizierung übergeben
            mapped_answer=classification(answer,classification_prompt)
            print("next question:", mapped_answer.lstrip())
            
    with open('log.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(log)


    return True
