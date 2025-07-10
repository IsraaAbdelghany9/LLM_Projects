# LLM_Projects
This repository houses a collection of diverse projects leveraging Large Language Models (LLMs). My goal is to continuously develop my skills in prompt engineering, fine-tuning, and integrating LLMs, while creating practical and innovative applications.


## NoteBooks:

1. `001_website_scrapping_summerizing`
    - That is a small Project that scrap given URL and summerize it
    - it can be added in a larger task later on 

2. `002_LangChain_Tutorial`
    - That notebook is to start with langchain and test its code how it is working with gemini 
    - Almost all taken from the documentation [langchain_google_generative_ai](https://python.langchain.com/docs/integrations/chat/google_generative_ai/)

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