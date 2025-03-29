"USES KEY,VALUE PAIRS"

Stanley= {"l_name": "Mwitwari", "Age":19, "Country": "Kenya"}
# print(Stanley["l_name"])

Stanley["Age"]=20
# print(Stanley)

# to remove a key value pair
# Stanley.pop("Age")
# print(Stanley)

# .get method
# print(Stanley.get("Age"))

print(Stanley.items())

for i,j in Stanley.items():
    print(f"The info for Stanley is: {i}:{j}")
