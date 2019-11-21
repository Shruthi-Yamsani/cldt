import requests
import sys

#API details
apihost = 'https://fourtytwowords.herokuapp.com'
apikey = "b972c7ca44dda72a5b482052b1f5e13470e01477f3fb97c85d5313b3c112627073481104fec2fb1a0cc9d84c2212474c0cbe7d8e59d7b95c7cb32a1133f778abd1857bf934ba06647fda4f59e878d164"
endpoints = {"randomWord" : "randomWord", "definitions" : "definitions", "examples" : "examples", "relatedWords" : "relatedWords"}


#Read User input
action = sys.argv[1]
word = sys.argv[2]
print(action, word)
