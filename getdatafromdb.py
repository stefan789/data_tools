import cloudant
import json
import codecs

# Authentication
acct = cloudant.Account(uri="http://raid.nedm1:5984")
res = acct.login(user, pw)
assert res.status_code == 200

# Grab the correct database
db = acct["nedm%2Ffluxgate"]

# Reads all data from a certain time
des = db.design("document_type")
the_view = des.view("document_type")

# Can read all data with a certain key from a certain time
results = the_view.get(params=dict(
                                   endkey={},
                                   startkey=['log', 2015, 4, 19, 1, 00],
                                   include_docs=True,
                                   reduce=False
                                   )
                      ).json()
all_ids = [(i["id"], (i["doc"]["log"], i["doc"]["timestamp"])) for i in  results['rows']]

ldes = db.design("log")
lthe_view = ldes.view("log")

# Grab all the data
keys=map(lambda x: [x[0], "data"], all_ids)
r = lthe_view.post("?reduce=false&include_docs=true", data=json.dumps(dict(keys=keys))).json()

values = [(j["Bx"], j["By"], j["Bz"]) for j in map(lambda x : x["doc"]["value"], r["rows"])]

with codecs.open("data.txt", "w", "utf-8") as f:
    for logt, vals in zip(all_ids, values):
        _, (l, t) = logt
        print t, vals, l
        f.write(unicode(t) + unicode("\t") + unicode(vals) + unicode("\t")+ unicode(l) + unicode("\n"))
