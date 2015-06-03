__version__ = '1.0'

from pyquery import PyQuery as pq
import requests
import sys
from pymongo import MongoClient
import datetime
import json

def get_ids(_id="chambers"):
    html = requests.get("http://wwwin-tools.cisco.com/dir/reports/"+_id)
    d = pq(html.content)
    f = lambda x: x.text
    return map(f,d("table#rcTable tbody tr td:nth-child(4) a"))

def get_under_ids(_id="chambers"):
    _ids = get_ids(_id)
    return _ids[_ids.index(_id)+1:]

def get_under_ids_rec(_id="chambers"):
    _ids = get_under_ids(_id)
    if _ids == []:
        return _id
    else:
        return {_id: map(get_under_ids_rec, _ids)}

def main():
    root_id = sys.argv[1]
    id_dict = get_under_ids_rec(root_id)
    doc = dict(id_dict=id_dict,
               update_time=datetime.datetime.utcnow(),
               cralwer_version=__version__)
    
    client = MongoClient('localhost', 27017)
    client.Cisco.PeopleDirectory.insert(doc)
    print json.dumps(id_dict, indent=2)

if __name__ == '__main__':
    main()