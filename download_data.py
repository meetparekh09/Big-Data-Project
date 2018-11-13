from google_ngram_downloader import readline_google_store


fname, url, records = next(readline_google_store(ngram_len=2))

with open('google-all-2grams', 'w') as file:
    record = next(records)
    while record:
        file.write(record.ngram + '\t' + str(record.year) + '\t' + str(record.match_count) + '\t' + str(record.volume_count) + '\n')
        file.flush()
        # print(record)
        record = next(records)
