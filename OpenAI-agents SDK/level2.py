from pydantic import BaseModel

class WeatherInfo(BaseModel):
    location: str
    temperature: float
    unit: str = "C"

w = WeatherInfo(location="Karachi", temperature=29.5)

# print("dict:", w.model_dump())   # Python dict
# print("json:", w.model_dump_json())   # JSON string

print("json indent:", w.model_dump_json(indent=2))
print("json exclude:", w.model_dump_json(exclude={"unit"}))