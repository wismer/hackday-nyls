import json
import cPickle as pickle


def unpack(filename="accidents.p"):
  data=pickle.load(open(filename,"rb"))
  jsonfile = open("data.json", "wb")
  jsondata=json.dumps(data)
  jsonfile.write(jsondata)

  return jsondata


unpack()