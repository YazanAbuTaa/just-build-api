from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List

# Load up LLM
GROQ_API_KEY = ""
llm = ChatGroq(model_name ="openai/gpt-oss-120b", api_key=GROQ_API_KEY)


# Define output formatter
class BaseOutputFormat(BaseModel):
    name: str = Field(description="product name")
    price: float = Field(description="Product price in USD")
    features: List[str] = Field(description="List of product features")

parser = JsonOutputParser(pydantic_object=BaseOutputFormat)


prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract product information from the user's query.\n{format_instructions}"),
    ("user", "{query}")
])

# Chain it together
chain = prompt | llm | parser

result = chain.invoke(
    {"query": "I want a laptop that costs 99 with features like: google support, microsoft support and dahua support. And I want it to be razor manufactured.",
    "format_instructions": parser.get_format_instructions()})


print(result['name'])