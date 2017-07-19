# Tweet-Clustering-Function using k-means.

Twitter provides a service for posting short messages. 

In practice, many of the tweets are very similar to each other and can be clustered 
together. 

By clustering similar tweets together, we can generate a more concise and organized representation of the raw tweets, which will 
be very useful for many Twitter-based applications (e.g., truth discovery, trend analysis, search ranking, etc.)

And in this project we clustered tweets using Jaccard Distance metric and K-means clustering.

The Jaccard Distance between two sets is defined as the difference of the sizes of the union and the intersection of two sets 
divided by the size of the union of the sets.



Instructions to run code:
1. Please ensure that you are running your code on Python 2.7 compiler
2. Should have the current folder pointing to Part-2
3. Need to have the input files 'InitialSeeds.txt' and 'Tweets.json' present in the folder Part-2

The libraries used were: json, csv

Run the program, tweets-k-means.py as follows:
>>>python tweets-k-means.py <numberOfClusters> <initialSeedsFile> <TweetsDataFile> <outputFile>

For example,
>>>python tweets-k-means.py 25 InitialSeeds.txt Tweets.json tweets-k-means-output.txt
