import argparse
import re


def load_data(filepath):
    with open(filepath, "rt", encoding='utf8') as file_with_text:
        return file_with_text.read()


def get_most_frequent_words(text_study):
    tmpl = r'[\w\-]+'
    words_all = re.findall(tmpl, text_study)
    statistic_frequent_words = []
    for word in set(words_all):
        statistic_frequent_words.append((words_all.count(word), word))
    statistic_frequent_words.sort(reverse=True)
    return statistic_frequent_words[:10]


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
    print("10 самых употребимых слов:")
    templ = '{1} - встречается {0} раз'
    for stat_unit in statistic_words:
        print(templ.format(*stat_unit))


def main():
    filepath = parse_filepath()
    text_study = load_data(filepath)
    statistic_words = get_most_frequent_words(text_study)
    print_statistic(statistic_words)

if __name__ == '__main__':
    main()
