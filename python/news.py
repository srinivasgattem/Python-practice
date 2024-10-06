import json
import requests
news=input("what type of news you want to know about:")
url= f"https://www.fairobserver.com/?gad_source=1&gclid=Cj0KCQjw5ea1BhC6ARIsAEOG5pxEjq_HdEPUocohUuyFc507c2Cor6qC6-7TdJsZALkMcttmyLGcvM4aAj-2EALw_wcB#gad_source=1"
r=requests.get(url)
print(r.text)