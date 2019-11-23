import requests
import sys
import random

# API details
apihost = 'https://fourtytwowords.herokuapp.com'
apikey = "b972c7ca44dda72a5b482052b1f5e13470e01477f3fb97c85d5313b3c112627073481104fec2fb1a0cc9d84c2212474c0cbe7d8e59d7b95c7cb32a1133f778abd1857bf934ba06647fda4f59e878d164"
action_endpoints = {"defn": "definitions", "ex": "examples", "syn": "relatedWords", "ant": "relatedWords", "play": "",
                    "wod": "randomWord"}

def pickRandomWord():
	url = apihost + "/words/" + action_endpoints["wod"] + "?api_key=" + apikey
	response = requests.get(url)
	return response.json()["word"]
	
def play(defn, syn, ant, ex, word, number_trial):
    index = number_trial - 1
    print("Guess the word based on below details")
    
    if defn:
        print("The definition is:")
        if index < len(defn):
            print (defn[index])
        else:
            print (defn[0])
    
    if syn:
        print("The synonym is:")
        if index < len(syn):
            print (syn[index])
        else:
            print (syn[0])
    
    if ant:
        print("The antonym is:")
        if index < len(ant):
            print (ant[index])
        else:
            print (ant[0])
            
    #Read User input as answer
    answer = input("Enter your Answer: ")
    #Validate user answer
    if answer == word:
        print("Success! You won!")
    else:
        print("Wrong Answer")
        print("Press 1 to Try Again")
        print("Press 2 if you need a hint")
        print("Press 3 to Quit")
        choice = input()
        if choice == "1":
            actions = ["defn", "syn", "ant", "ex"]
            word = pickRandomWord()
            play(defn, syn, ant, ex, word, number_trial+1)
        elif choice == "2":
            print("The word in jumbled format: ",''.join(random.sample(word,len(word))))
            play(defn, syn, ant, ex, word, number_trial+1)
        else:
            print("You are out now! Thanks for trying us")

#Read User input
actions = None
word = None
isPlay = False
number_of_inputs = len(sys.argv) - 1
if number_of_inputs >= 1:
	argv1 = sys.argv[1]
	if argv1 == "play":
		isPlay = True
		actions = ["defn", "syn", "ant", "ex"]
		word = pickRandomWord()
	elif argv1 in action_endpoints:
		actions = [argv1]
		word = sys.argv[2]
	else:
		actions = ["defn", "syn", "ant", "ex"]
		word = argv1
else:
	actions = ["defn", "syn", "ant", "ex"]
	word = pickRandomWord()
	
	

# Implement respective API for given input
defn = []
ex = []
syn = []
ant = []

if actions is not None:
    for action in actions:
        if action in ["defn", "syn", "ant", "ex"]:
            url = apihost + "/word/" + word + "/" + action_endpoints[action] + "?api_key=" + apikey
            response = requests.get(url)
            if response.status_code == 200:
                if action == "ex":
                    for text in response.json()["examples"]:
                        ex.append(text['text'].capitalize())
                elif action == "syn":
                    for related in response.json():
                        if related['relationshipType'] == 'synonym':
                            for wrd in related['words']:
                                syn.append(wrd.capitalize())
                elif action == "defn":
                    for dfn in response.json():
                        defn.append(dfn["text"].capitalize())
                elif action == "ant":
                    for related in response.json():
                        if related['relationshipType'] == 'antonym':
                            for wrd in related['words']:
                                ant.append(wrd.capitalize())
            else:
                print("Error connecting ", action_endpoints[action], " End point")

if not isPlay:
    if len(defn)> 0:
        print("\n Definition of ",word.capitalize(), "\n")
        for d in defn:
            print (d)
    if len(syn)>0:
        print("\n Synonyms for word ",word.capitalize(), "\n")
        for s in syn:
            print (s)
    if len(ant)>0:
        print("\n Antonyms for word ",word.capitalize(), "\n")
        for a in ant:
            print (a)
    if len(ex)>0:
        print("\n Examples for word ",word.capitalize(), "\n")
        for e in ex:
            print (e)
            
else:
    number_trial = 1
    play(defn, syn, ant, ex, word, number_trial)
