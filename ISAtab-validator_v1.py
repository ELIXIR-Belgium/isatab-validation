from sys import argv
from isatools import isatab
import os
import json
import codecs
from tempfile import TemporaryDirectory

# Parameters
# ----------

isa_config_dir = "./isaconfig-phenotyping-basic"
isa_tab_dir = argv[1]

# Converting all characters to UTF-8
# ----------------------------------

files = [f for f in os.listdir(isa_tab_dir) if f.endswith('.txt')]

with TemporaryDirectory() as tmpdirname:
    print('Created temporary directory:', tmpdirname)
    print('Converting files to UTF-8.')
    for f in files:
        with codecs.open(isa_tab_dir + os.sep + f, 'r') as file:
            lines = file.read()
        with codecs.open(tmpdirname + os.sep + f, 'w', encoding='utf8') as file:
            file.write(lines)

    # Validating ISA-TAB with configuration files
    # -------------------------------------------

    try:
        print('Validating isa-tab files against configuration files found in ' + isa_config_dir)
        validation_log_path = isa_tab_dir + os.sep + 'validation_log.json'
        report = isatab.validate(
            open(os.path.join(tmpdirname, 'i_investigation.txt')), isa_config_dir)
        with open(validation_log_path, 'w') as out_fp2:
            json.dump(report, out_fp2, indent=4)

        print('VALIDATION FINISHED')
        print("* Errors found: {}\n* Warnings found: {}\n* Info messages: {}".format(
            len(report['errors']), len(report['warnings']), len(report['info'])))
        print('The ISA-TAB validation log file can be found at: ' +
              validation_log_path)

    except Exception as ioe:
        print('ISA-TAB validation failed!...')
        print(str(ioe))
