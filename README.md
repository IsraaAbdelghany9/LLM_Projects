# LLM_Projects
This repository houses a collection of diverse projects leveraging Large Language Models (LLMs). My goal is to continuously develop my skills in prompt engineering, fine-tuning, and integrating LLMs, while creating practical and innovative applications.


## NoteBooks:

1. `001_website_scrapping_summerizing`
    - That is a small Project that scrap given URL and summerize it
    - it can be added in a larger task later on 

2. `002_LangChain_Tutorial`
    - That notebook is to start with langchain and test its code how it is working with gemini 
    - Almost all taken from the documentation [langchain_google_generative_ai](https://python.langchain.com/docs/integrations/chat/google_generative_ai/)

3. `003_LangChain_Tutorial_2`
    - This notebook is to try the PromptTemplate from langchain_core 
    - It can be used in all other projects it is easier to use if you have var in the prompt

4. `004_LinkedIn_Scraping` 
    - scraps LinkedIn profiles using URL and get info then summerize it using llm 
> To get the api key of scrapin check : [Scrapin](https://app.scrapin.io/api)

## Helper scripts 
### 1. gemini_models_print.py

you may want to change the model name that i am using, I had an error before because of the model name so added that script to help not to fall in that  again you can edit it to get the name you want like 

```python
for model in models:
    if "flash" in model.name:
        print(model.name)

## OR

for model in models:
    if model.name.endswith("generation"):
        print(model.name)

```

That will save more time 

## Note About Black and nbqa
It is my first use so i wanted to add a short info about them if you are interested too

- **🖤 Black** is a **Python code formatter** that automatically formats your code to follow best practices (PEP8), making it clean and consistent. Just run it, and it reformats the code without needing manual edits.

- **📓 nbqa** lets you use **Black (and other tools)** directly on **Jupyter Notebooks** (`.ipynb`). It applies the formatting to the code cells while keeping everything else (like markdown and outputs) unchanged.

✅ Use `black` for `.py` files
✅ Use `nbqa black` for `.ipynb` files


