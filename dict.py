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
	actions = ["wod"]
	
#Implement respective API for given input
if actions is not None:
	for action in actions:
		if action in ["defn", "syn", "ant", "ex"]:
			url = apihost + "/word/" + word + "/" + action_endpoints[action] + "?api_key=" + apikey
			response = requests.get(url)
			if action == "ex":
				for text in response.json()["examples"]:
					print(text['text'])
		else:
			url = apihost + "/words/" + action_endpoints[action] + "?api_key=" + apikey
		
		

			
		
