from . import models

def winning_bid(ItemListing):
    item = models.ItemListing.get.all(pk=ItemListing.item_id)
    highest = 0
    if item.bids == None:
        return 0
    for i in item.bids:
        if i.bid > highest:
            winningBid = i
        else:
            pass
    return winningBid