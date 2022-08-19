"""
 *  Description: Code Melli Generator is a python class for generating Iranians national code by area code
 *  Author: Mohammadreza Naderi
 *  Github: https://github.com/naderidev
 --> type -h for help
"""
import argparse

from classes.CodeMelliGenerator import CodeMelliGenerator

if __name__ == '__main__':
    print(__doc__)
    parser = argparse.ArgumentParser(description=__doc__)
    required = parser.add_argument_group('required arguments')
    required.add_argument('-a', '--areacode', type=int, help='area code', required=True)
    required.add_argument('-s', '--save', type=str, help='file path for save codes', required=True)

    notrequired = parser.add_argument_group('not required arguments')
    notrequired.add_argument('-psl', '--print_status_live', action='store_true',
                             help='print status in live | ATTENTION: printing status in live will decrease speed ')

    args = parser.parse_args()
    cmg = CodeMelliGenerator(area_code=args.areacode, print_status_live=args.print_status_live)
    cmg.generate()

    db = open(args.save, 'w+')
    for _code in cmg.get_codes():
        db.write(f"{_code}\n")
    db.close()
    print('\nAll codes saved!')
