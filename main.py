import argparse

from nlp2sql import NLP2sql


def main():
    arg_parser = argparse.ArgumentParser(description='Natural Language to SQL query')
    arg_parser.add_argument('-d', '--database', help='Path to SQL dump file', default="~\school.sql")
    arg_parser.add_argument('-l', '--language', help='Path to language configuration file', default="~\english.csv")
    arg_parser.add_argument('-i', '--sentence', help='Input sentence to parse', required=True)
    arg_parser.add_argument('-j', '--json_output', help='path to JSON output file', default=None)
    arg_parser.add_argument('-t', '--thesaurus', help='path to thesaurus file', default=None)
    arg_parser.add_argument('-s', '--stopwords', help='path to stopwords file', default=None)

    args = arg_parser.parse_args()


    query_parsing = NLP2sql(database_path=args.database,
    language_path=args.language,
    thesaurus_path=args.thesaurus,
    json_output_path='./output.json').get_query(args.sentence)

if __name__ == '__main__':
    main()
