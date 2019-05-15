from isatools import isatab
import sys
import os
import json

isa_config_dir = "./isaconfig-phenotyping-basic"
isa_tab_dir = sys.argv[1]

report = isatab.validate(open(os.path.join(isa_tab_dir, 'i_investigation.txt')), isa_config_dir)


print(json.dumps(report, indent=4))