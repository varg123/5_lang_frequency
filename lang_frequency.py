import argparse
import re
import collections

COUNT_UNIT_STATISTIC = 10


def load_data(filepath):
    with open(filepath, 'rt', encoding='utf8') as file_with_text:
        return file_with_text.read()


def get_most_frequent_words(text_study):
    tmpl = r'[\w\-]+'
    words_all = re.findall(tmpl, text_study)
    statistic_frequent_words = collections.Counter()
    for word in words_all:
        statistic_frequent_words[word] += 1
    return statistic_frequent_words.most_common(COUNT_UNIT_STATISTIC)


def parse_filepath():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--filepath',
        required=True,
        help='the file with text'
    )
    namespace = parser.parse_args()
    return namespace.filepath


def print_statistic(statistic_words):
    templ_header = '{} самых употребимых слов:'
    templ_unit_stat = '{0} - встречается {1} раз'
    print(templ_header.format(COUNT_UNIT_STATISTIC))
    for stat_unit in statistic_words:
        print(templ_unit_stat.format(*stat_unit))


def main():
    filepath = parse_filepath()
    try:
        text_study = load_data(filepath)
    except FileNotFoundError:
        exit('Файл с текстом не найден')
    statistic_words = get_most_frequent_words(text_study)
    print_statistic(statistic_words)

if __name__ == '__main__':
    main()
