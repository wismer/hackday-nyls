import json
import cPickle as pickle


def unpack(filename="accidents.p"):
	data=pickle.load(open(filename,"rb"))
	jsondata=json.dumps(data)
	return jsondata