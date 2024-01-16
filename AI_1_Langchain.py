import openai
from langchain import *

# LLM - Large Language Model, and you can do a lot they have reduced your headache
# It's like having billions or trillions of data
# Here temperature means randomness, more temperature more randomness 0 to 1
llm = OpenAI(temperature=0.3, openai_api_key="")

# print(llm.predict("What is the capital of rome")) #TODO: it will give results like chatgtp
#Todo: Making template
prompt = PromptTemplate.from_template("What is the capital of {place}")
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("Place")) #template parameter gives here
print(chain.run("Multan")) #template parameter gives here