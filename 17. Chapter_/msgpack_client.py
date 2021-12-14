from msgpackrpc import Client, Address

client = Client(Address("localhost", 6789))
num = 8
result =  client.call('double', num)
print("Dwukrotność liczby %s jest równa %s" % (num, result))
