from jsonrpcclient import request

num = 7
response = request("http://localhost:5000", "double", num=num)
print("Dwukrotność liczby", num, "jest równa", response.data.result)
