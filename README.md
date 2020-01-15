# Hotel Reservation Spoken Human Robot Interaction
In this project, our aim is to implement a task oriented SDS in a specific hotel reservation scenario. 

### Pipeline
-	Acquires a spoken sentence
-	Calls the ASR to get the corresponding text
-	Calls DP, prints the dependency graph 
-	Returns some info through the text-to-speech

### Usage

This program is built using the following versions:
Python 3.7

Install the dependencies.

```sh
$ pip install speechrecognition
$ pip install pipwin
$ pipwin install pyaudio
$ pip install spacy
$ pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
$ pip install nltk
```
Espeak also needs to be installed and added to the path.

- [Espeak][df1]


[df1]: <http://espeak.sourceforge.net/>


### Future Work

Encapsulation and Inheritance for the methods
