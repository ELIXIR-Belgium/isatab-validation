# ISA-tab validation
Using the python API from ISA to validate isa-tab files for MIAPPE compliance.

The validator makes use of the configuration files found on the MIAPPE [github](https://github.com/MIAPPE/ISA-Tab-for-plant-phenotyping/tree/v1.1).

Because the validator is sensitive to non UTF-8 characters, all files get temporarily converted to UTF-8 by default.

### Usage

```bash
python ISAtab-validator_v1.py <path to isatab directory>
```

### Output

The validation log file can be found in the same directory as the ISA-tab files named `validation_log.json`
