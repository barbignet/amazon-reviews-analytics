import json
import snap

reviewers = None
reviewers_id_cache = dict()
current_user_id = 1

# Load local database object
with open('reviewers.json', 'rb') as fp:
    reviewers = json.load(fp)

print 'Loaded ' + str(len(reviewers)) + ' reviewers'

################# Collaboration Graph ################
# node is reviewer
# same product is link
collab_graph = snap.TUNGraph.New()

# Add nodes and create translation directory
for reviewer in reviewers:
    reviewers_id_cache[current_user_id] = reviewer
    collab_graph.AddNode(current_user_id)
    current_user_id += 1

for NI in collab_graph.Nodes():
    print reviewers_id_cache[NI.GetId()]

# Add links between nodes?
