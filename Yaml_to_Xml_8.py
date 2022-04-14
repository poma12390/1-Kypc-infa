import yaml
from dicttoxml import dicttoxml
import time
start_time = time.time()

with open("table1.yaml", 'r', encoding="utf-8") as stream:
    parsed_yaml = yaml.safe_load(stream)
    print(parsed_yaml)
    xml = dicttoxml(parsed_yaml)
    print(xml)
print('%.5f' % ((time.time() - start_time)*10),"seconds")