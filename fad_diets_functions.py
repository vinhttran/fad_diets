# function to search for words in a tweet
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

# function to create a new column in the dataframe with keyword mentions
def keyword_column_boolean(df, keyword_list):
    for x in keyword_list:
        df[x] = df['text'].apply(lambda text: word_in_text(x,text))

def count_of_keywords(df, keyword_list):
    count = []
    for x in keyword_list:
        count.append((pd_tweets_en[x].value_counts()[True]))
    return count

def count_of_keywords_by(df, keyword, diet_list):
    pd_tweets_en[keyword] = pd_tweets_en['text'].apply(lambda text: word_in_text(keyword, text))
    count_list = []
    for x in diet_list:
        count_list.append( pd_tweets_en[pd_tweets_en[keyword] == True][x].value_counts()[True])
    return count_list

def count_of_keywords_by_false(df, keyword, diet_list):
    pd_tweets_en[keyword] = pd_tweets_en['text'].apply(lambda text: word_in_text(keyword, text))
    count_list = []
    for x in diet_list:
        count_list.append( pd_tweets_en[pd_tweets_en[keyword] == False][x].value_counts()[True])
    return count_list

def welch_test_statistic(sample_1, sample_2):
    numerator = np.mean(sample_1) - np.mean(sample_2)
    denominator_sq = (np.var(sample_1) / len(sample_1)) + (np.var(sample_2) / len(sample_2))
    return numerator / np.sqrt(denominator_sq)

def welch_satterhwaithe_df(sample_1, sample_2):
    ss1 = len(sample_1)
    ss2 = len(sample_2)
    df = (
        ((np.var(sample_1)/ss1 + np.var(sample_2)/ss2)**(2.0)) /
        ((np.var(sample_1)/ss1)**(2.0)/(ss1 - 1) + (np.var(sample_2)/ss2)**(2.0)/(ss2 - 1))
    )
    return df

def count_winning_pairs(sample_1, sample_2):
    sample_1, sample_2 = np.array(sample_1), np.array(sample_2)
    n_total_wins = 0
    for x in sample_1:
        n_wins = np.sum(x > sample_2) + 0.5*np.sum(x == sample_2)
        n_total_wins += n_wins
    return n_total_wins
