


import requests
#Beautiful Soup is a library that makes it easy to scrape information from web pages
from bs4 import BeautifulSoup
#!pip install transformers
from transformers import pipeline
import csv

#this method eill allow the web scrapping to happen 
#i used "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/" to guide me 
def web_scrapping(topic):
    

    #using the google as the search engine
    url = f"https://www.google.com/search?q={topic}"

    #got this from "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    }
    response = requests.get(url, headers=headers)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html5lib')

    # this will gather the important or relevant information
    results = soup.find_all("div", class_="BNeawe")

    return results

#got this from https://towardsdatascience.com/question-answering-with-pretrained-transformers-using-pytorch-c3e7a44b4012
# Function to answer user questions using transformers' question-answering model
#narrows the answer
def get_answer(context, question):
    #using natural language processors
    r= pipeline("question-answering")
    answer = r(question=question, context=context)
    return answer["answer"]


#main program gets user input
def main():
    
    # use input 
    topic = input("Enter a topic: ")

    # Search the web for information about the topic
    results = web_scrapping(topic)
    # getting the context that will be necessary when pilelining
    context = " ".join(result.text for result in results)

    # user input questuon
    while True:
        question = input( "Ask a question  based on " + topic + " (or type 'quit' to exit query): ")
        #exit the loop
        if question.lower() == "quit":
            break #ends loop
        #prints out the question
        answer = get_answer(context, question)
        print("Answer:", answer)


if __name__ == "__main__":
    main()
