"""
The task is to design and write a program which takes care of a silent auction.

The program should start off by asking for the bidding item, and the reserve price, which is requested from the auction manager before the auction starts. It should then repeatedly: show the highest bid so far, ask for a bid, and check if the bid placed is higher than the highest bid so far. If it is a higher bid, store the bid. Otherwise show a “need a higher bid” message.

The program needs a way of being terminated by the user. Build in some prearranged signal value (e.g. a bid of -1) to end the loop on demand.

When the user stops the input loop, the highest bid should be checked to see if it beat the reserve. If the reserve price is met, the highest bid should be displayed. If not, a message saying the object didn't sell should be displayed.
an example of the output:
"
"""