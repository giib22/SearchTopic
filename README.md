# SearchTopic
Program that accepts a topic as a string input from the user, searches the internet for information about it, and answers any questions regarding the topic.

Program contains Web Scrapping, and pipelines. 

There will be the requirements of third party instalations:

- **pip install transformers**
- **pip install requests**
- **pip install html5lib**
- **pip install bs4**

In this program, I  first defined a method **web_scapping()**. This uses web scraping using the function **BeautifulSoup**. It searches Google.com for the topic that the user inputs and extracts relevant information from the search results. 
Resources: https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/


The method **answer_question()** that uses the transformers natural language processors **question-answering pipeline**. It takes a context (extracted from the web_scrapping method) and a question(user input), and returns the answer based on what the pipeline answer.
Resources: https://towardsdatascience.com/question-answering-with-pretrained-transformers-using-pytorch-c3e7a44b4012


In the **main()** function, the program takes the user input, search the web for the topic, and extracts the context. Then, there is a loop where the program prompts the user to ask questions based on the topic. Once the question is answered the user has the chance to enter another question or exit the program.

In this program I referenced the pages:
- https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
- https://towardsdatascience.com/question-answering-with-pretrained-transformers-using-pytorch-c3e7a44b4012
