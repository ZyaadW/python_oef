import io
import requests
with io.open("inhoud_van_website.txt","w",encoding='utf8') as f:
    r = str(requests.get("https://mosa-rt.be"))
    f.write(r)
with io.open("inhoud_van_website.txt","r",encoding='utf8') as f:
    inhoud = f.read()

print(inhoud)    
f.close()