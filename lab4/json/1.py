import json

with open('C:\\Users\\ASUS\\OneDrive\\Рабочий стол\\pp2\\pp2\\lab4\\json\\sample_data.json') as file:
    data = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

imdata = data["imdata"]
for dat in data["imdata"]:
    item = dat["l1PhysIf"]
    attributes = item["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"] 
    mtu = attributes["mtu"]
    print(dn + " "*30 + speed + " "*3 + mtu)
