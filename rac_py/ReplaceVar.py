fr = open("/Users/mthakur/Downloads/db.properties").readlines()
fw = open("/Users/mthakur/Downloads/dbc.properties", "w")
str=""
for line in fr:
  if "PORT" not in line:
    str += line
    print str
str += "PORT=7000\n"
print str
fw.write(str)
fw.close()