def query_word_distribution(search_queries):

    total_queries = len(search_queries)
    word_count_stats = {}

    for query in search_queries:
        word_count = len(query.split())
        word_count_stats[word_count] = word_count_stats.get(word_count, 0) + 1

    for words_count, count in sorted(word_count_stats.items()):
        percent = (count / total_queries) * 100

        if words_count == 1:
            word_label = "слово"
        elif 2 <= words_count <= 4:
            word_label = "слова"
        else:
            word_label = "слов"

        print(str(words_count) + " " + word_label + ": " + str(round(percent)) + "%")
