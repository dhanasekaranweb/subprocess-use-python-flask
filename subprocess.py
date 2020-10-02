import pickle
import sys

#read the input
data = pickle.loads(sys.stdin.buffer.read())


message = data["message"]

#you can write your custom logics and stuffs

#object/array send back
output = {"message":"Hai this is the output"}
datas = pickle.loads(pickle.dumps(output))
sys.stdout.buffer.write(pickle.dumps(datas))