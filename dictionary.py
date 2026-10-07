data = {
    "nama": "Ihsan",
    "umur": 25,
    "baju" : "putih"
}

print(data["nama"])

data["kota"] = "Tangerang"

print(data)

data["umur"] = 31

print(data)

del data["baju"]

print(data)


for key in data:
    print (key, data[key])

for key, value in data.items():
    print(key,value)