import json

reviewers = None

# Load local database object
with open('reviewers.json', 'rb') as fp:
    reviewers = json.load(fp)

print 'Loaded ' + str(len(reviewers)) + ' reviewers.'

################# Calculate top reviewers ################
reviews_count = dict()
user_id = 0

for reviewer in reviewers:
    reviews_count[user_id] = (reviewer, len(reviewers[reviewer]))
    user_id += 1

# Sort reviewers by reviews count
top_reviewers = sorted(reviews_count.items(), key=lambda x: x[1][1], reverse=True)

# Print TopX reviewers IDs
top_limit = 100
for i in range(top_limit):
    print top_reviewers[i]
