from agents import Agent, Runner, function_tool
from agent_config import config
import os
from dotenv import load_dotenv
import requests
load_dotenv()
api_key=os.getenv("WEATHER_API_KEY")
@function_tool
def get_weather(city:str)->str:
                                                        #  end point    api key   and q=city
    response= requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}")
    data=response.json()  # response.jason=python built-in method, jo api se aye raw response ko readable data yani dict m convert krta, k python kya h usy easily smjh sakta h.
    return f"The Weather in {city} is {data['current']['temp_c']}C with {data['current']['condition']['text']}."
    # first we store URL in response, then response ko json m convert karwa kar usy data m store karwaya, 
    # phr data ko use kiya hard coded return k liye
agent = Agent(
    name="Weather Agent",
    instructions="You are a helpful assistant",
    tools=[get_weather])
result = Runner.run_sync(agent,
                         "What is the weather in Islamabad?",
                         run_config=config)
print(result.final_output) 