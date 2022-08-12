# How to run the code
python convert_ilmt_to_universal_pos_tag.py --input sample-hin-ilmt.txt --map ilmt_to_universal.json --output sample-hin-universal.txt

## input file should be in conll format, each line is of the format "token\tILMT-tag" and lines are separated by a blank line.
## ilmt_to_universal.json contains the mapping from ILMT to Universal POS tagset
## output file will be generated in the same format "token\tUniversal-tag" and lines are separated by a blank line.
## This tool uses word lists where there is one to many mapping like CC to CCONJ and SCONJ; SYM to SYM and PUNCT