#!/usr/bin/env python
import sys
import json
import yaml

data = yaml.dump(yaml.load(json.dumps(json.loads(open(sys.argv[1]).read())), Loader=yaml.FullLoader))

print(data)

# print yaml.dump(yaml.load(json.dumps(json.loads(open(sys.argv[1]).read()))), default_flow_style=False)
