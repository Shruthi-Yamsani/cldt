import requests
import sys

#API details
apihost = 'https://fourtytwowords.herokuapp.com'
apikey = "b972c7ca44dda72a5b482052b1f5e13470e01477f3fb97c85d5313b3c112627073481104fec2fb1a0cc9d84c2212474c0cbe7d8e59d7b95c7cb32a1133f778abd1857bf934ba06647fda4f59e878d164"
action_endpoints = {"defn" : "definitions", "ex" : "examples", "syn" : "relatedWords", "ant" : "relatedWords", "play" : "", "wod" : "randomWord"}

#Read User input
actions = None
word = None
number_of_inputs = len(sys.argv)-1
if number_of_inputs >= 1:
	argv1 = sys.argv[1]
	if argv1 == "play":
		actions = [argv1]
	elif argv1 in action_endpoints:
		actions = [argv1]
		word = sys.argv[2]
	else:
		actions = ["defn", "syn", "ant", "ex"]
		word = argv1
else:
	actions = ["defn", "syn", "ant", "ex"]
	url = apihost + "/words/" + action_endpoints["wod"] + "?api_key=" + apikey
	response = requests.get(url)
	word = response.json()["word"]
	
#Implement respective API for given input
if actions is not None:
	for action in actions:
		if action in ["defn", "syn", "ant", "ex"]:
			url = apihost + "/word/" + word + "/" + action_endpoints[action] + "?api_key=" + apikey
			response = requests.get(url)
			if response.status_code == 200:
				if action == "ex":
					print("\n Examples for word ",word.capitalize(), "\n")
					for text in response.json()["examples"]:
						print(text['text'].capitalize())
				elif action == "syn":
					print("\n Synonyms for word ",word.capitalize(), "\n")
					for related in response.json():
						if related['relationshipType'] == 'synonym':
							for wrd in related['words']:
								print(wrd.capitalize())
				elif action == "defn":
					print("\n Definition of ",word.capitalize(), "\n")
					for dfn in response.json():
						print(dfn["text"].capitalize())
				elif action == "ant":
					print("\n Antonyms for word ",word.capitalize(), "\n")
					for related in response.json():
						if related['relationshipType'] == 'antonym':
							for wrd in related['words']:
								print(wrd.capitalize())
			else:
				print("Error connecting ", action_endpoints[action], " End point")
			
		
		

			
		
