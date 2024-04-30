Here is the link to the documentation: https://docs.google.com/document/d/1cukdjkRARpjebGkFrNoECOg85tfZdxiQoOb1Nul-EgE/edit?usp=sharing


Testing Open Source LLM Models
Step 1: Downloading
Download Ollama from ollama.com.

Step 2: Installing Ollama
Search for models that can run on your own PC to host your own API. Running your own LLM model offers the advantage of having control over it and the option to fine-tune the model. Another key benefit is the absence of limits on API requests. While many open-source models can be accessed via API some require payment for each request in the form of tokens for input and output.

Step 3: Setting Up Your Own LLM Model
Write your own model file for custom configuration.
Create a model using the command ollama create name -f model_filename.
After successful setup run the model with ollama run <name>.
Test the model locally in the console

Step 4: Setting Up a Server to Test the REST API
Start the server by typing ollama serve in the command line.
Then in the console  type ollama run Modelname to start the model for the server.
After this you can write Python code to access the model.
Step 5: Python Code
Step 6: Respons form the model in Python

Something : 
Before I began hosting my own model I researched LLM APIs online. Most models I found were paid services, charging for API access based on the number of tokens I also explored a platform called Replicate for hosting LLMs, but it also involved paying for each request, which could become costly. Therefore, I decided to try hosting it myself, despite the initial investments required. It took some effort, but eventually, I managed to successfully host a functioning LLM with a REST API. Additionally, the hosted LLM runs on a machine with 16GB of RAM and utilizes only the CPU, without GPU acceleration. It's worth noting that the response times may be slightly delayed due to the computational power of my PC.


Replicate.com Pricing for API Request 




FinnHub 
FinnHub provides a fast API with freely accessible data that we can use to fetch live news and real-time data. With one API call per second, it's sufficient for our project to build a trading bot.

The price Plan : 


Use Case in the projekt :
In our project, we utilize Finnhub to get all current news and as a source to scrape the complete article. We also have the option to use the summarized variant to provide that to our LLM model.


Example  what we get form Finhub:
The datetime is in Unix. I also implement the formatting in the code before we store it in the CsV file.


All my Code solutions added in the Branch sprint1 Manuel !!! 

