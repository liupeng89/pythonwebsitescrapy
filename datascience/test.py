# from __future__ import division
# from collections import Counter
#
# interests = [
#         (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
#         (0, "Spark"), (0, "Storm"), (0, "Cassandra"),(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
#         (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
#         (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
#         (3, "statistics"), (3, "regression"), (3, "probability"),
#         (4, "machine learning"), (4, "regression"), (4, "decision trees"),
#         (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
#         (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
#         (6, "probability"), (6, "mathematics"), (6, "theory"),
#         (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
#         (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
#         (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
#         (9, "Java"), (9, "MapReduce"), (9, "Big Data")
# ]
#
# words_and_counts = Counter(word
#                            for usr, interest in interests
#                            for word in interest.lower().split())
#
# for word, count in words_and_counts.most_common():
#     if count > 1:
#         print word, ' : ', count
#
#
# for i in range(1, 10):
#
#     print i
#
#
# print 5 // 2
#
#
#
# print 5 / 2
#
#
#
#
#
#
#
#
#
from matplotlib import pyplot as plt

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
#
# plt.title('normal gdp')
#
# plt.ylabel('billon $')
#
# plt.show()


variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line
# because we've assigned labels to each series # we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=10)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

