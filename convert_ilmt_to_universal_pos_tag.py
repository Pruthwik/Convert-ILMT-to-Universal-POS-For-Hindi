"""Convert ILMT to Universal POS Tag."""
from argparse import ArgumentParser
from json import load
from re import search


def read_lines_from_file_and_remove_blanks(file_path):
    '''
    Read lines from a file and remove blank
    :param file_path: Path of the file to be read
    :return lines: List of lines after removing blank
    '''
    with open(file_path, 'r', encoding='utf-8') as file_read:
        return [line.strip() for line in file_read.readlines() if line.strip()]


def read_conll_file(file_path):
    '''
    :param file_path: Path of the Feature File
    :return Lines: Lines read from the feature file
    '''
    with open(file_path, 'r', encoding='utf-8') as finp:
        return finp.readlines()


def convert_ilmt_tags_to_universal_tags(lines, mapping, cconj, sconj, sym, punct):
    '''
    :param lines: Lines read from the feature file
    :param mapping: Dictionary containig mapping from ILMT to UT (Universal Tagset)
    :return changed_lines: Returns list of lines after changing the tags
    '''
    changed_lines = list()
    for line in lines:
        line = line.strip()
        if line:
            token, tag = line.split('\t')
            changed_tag = ''
            if search('CC.*', tag):
                print('HERE')
                if token in cconj:
                    print('HERE 2')
                    changed_tag = 'CCONJ'
                elif token in sconj:
                    changed_tag = 'SCONJ'
                else:
                    changed_tag = 'SCONJ'
            elif search('SYM.*', tag):
                if token in sym:
                    changed_tag = 'SYM'
                elif token in punct:
                    changed_tag = 'PUNCT'
                else:
                    changed_tag = 'SYM'
            else:
                for key in mapping:
                    if search(key, tag):
                        changed_tag = mapping[key]
                        break
            if not changed_tag:
                changed_tag = 'UNK'
            changed_lines.append(token + '\t' + changed_tag)
        else:
            changed_lines.append('')
    return changed_lines


def write_lines_to_file(out_path, lines):
    '''
    :param outpath: File path of the output file
    :param lines: Lines to be written into the file
    :return: None
    '''
    with open(out_path, 'w', encoding='utf-8') as fout:
        fout.write('\n'.join(lines) + '\n')


def read_json_file(file_path):
    '''
    :param file_path: Path of the JSON file containing the mapping
    :return mapping: Returns the mapping between the tagsets
    '''
    mapping = load(open(file_path, 'r', encoding='utf-8'))
    return mapping


def main():
    """Pass arguments and call functions here."""
    parser = ArgumentParser()
    parser.add_argument('--input', dest='inp', help='Enter the input file path')
    parser.add_argument('--map', dest='map', help='Enter the mapping file path')
    parser.add_argument('--output', dest='out', help='Enter the output file path')
    args = parser.parse_args()
    lines = read_conll_file(args.inp)
    mapping = read_json_file(args.map)
    cconj = read_lines_from_file_and_remove_blanks('word_lists/CCONJ.txt')
    sconj = read_lines_from_file_and_remove_blanks('word_lists/SCONJ.txt')
    sym = read_lines_from_file_and_remove_blanks('word_lists/SYM.txt')
    punct = read_lines_from_file_and_remove_blanks('word_lists/PUNCT.txt')
    changed_lines = convert_ilmt_tags_to_universal_tags(lines, mapping, cconj, sconj, sym, punct)
    write_lines_to_file(args.out, changed_lines)


if __name__ == '__main__':
    main()
