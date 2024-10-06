# How to run the script

Run the python script with the log file path (if you put it in the same folder as the code, then just the name is sufficent), similar to log file provide the tag mapping file as 2nd argument. You can also provide the ouput tag count file path/name as 3rd arg (optional) and ouput dstport and protocol count file path/name as 4rd arg (optional).

## sample command without output file :

`python3 Illumio_OA.py sample_log.txt sample_mapping.csv`

## sample command with output files name/path:

`python3 Illumio_OA.py sample_log.txt sample_mapping.csv output_tags_count.csv output_port_protocol.csv`

# Assumptions

1. Program only support default log format and version 2
2. The protocol number in log file won't have any unassigned protocols as per https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml i.e. from range 146-254, In such cases program ignores that log entry completely, as protocol name is not present in iana.org .
3. Assumed that two output files are required one for tags count and another for dstport,protocol count.
4. The code works for both log files as well as lookup csv having column header and also works if files dont have any column headers.
5. The folder contains a protocol.txt which contains protocol id and keyword mapping from https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml.

# Testing

1. Along with the sample test data provided, some test was generated and tested, different destination port and protocol were used. Also logs having unwanted data like protocol range from 146-254, was also included and the behaviour was tested.
2. Some sample log files are provided with the repo.
3. Code was tested with both log files and lookup csv having column headers or as well as not having column headers.

# Analysis

1. Understanding of amazon log file structure.
2. Building protocol map using https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml.
3. Based on above two analysis structure was designed where protocol.txt helped me in designing the dstport_protocol map from the log files where key is dstport:protocol_keyword and value is the count of the combination in the log file. This forms the basis of output file containing the count corresponding to dstport and protocol.
4. Similarly a tag map was created using the lookup table, where in key was dstport:protocol_keyword and value was the tag.
5. Lastly both the dstport_protocol map was iterated and the corresponding tag count was calculated.

Time complexity : O(n) + O(m) + O(p) , where n -> rows of log file, m -> rows of lookup table , p -> rows of protocols.

Space complexity : O(n) + O(m) + O(p), where n -> unique dstport,protocol count map , m -> dstport,protocol tag map and p -> protocol id and keyword map.
