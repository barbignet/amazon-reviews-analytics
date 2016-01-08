import gzip
import json

path = 'reviews_Video_Games.json.gz'

def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)

# reviewers dataset- reviewerID: { product_asin: timestamp,..}
reviewers = dict()

total_reviews = 0

for review in parse(path):
    reviewerID = review['reviewerID']
    #print reviewerID

    # Check if reviewer exists
    if reviewerID not in reviewers:
        reviewers[reviewerID] = dict()

    # product information-
    reviewd_productID = review['asin']
    reviewd_product_timestamp = review['unixReviewTime']

    # Check if product exists
    if reviewd_productID not in reviewers[reviewerID]:
        # Add to reviewed products
        reviewers[reviewerID][reviewd_productID] = reviewd_product_timestamp
        total_reviews += 1

    if total_reviews % 100000 == 0: print total_reviews

print reviewers

# save connections as json file to disk
with open('reviewers.json', 'wb') as fp:
    json.dump(reviewers, fp)

print 'Total reviewers: ' + str(len(reviewers))
print 'Total reviews: ' + str(total_reviews)
