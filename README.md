# MCM-ICM_2021
Finalist of Mathematical Contest in Modeling (MCM)® / Interdisciplinary Contest in Modeling (ICM)® 2021

**Problem D: The Influence of Music**

Summary:

In today's society, it has become more and more common to use "networks" connected by different nodes to analyze the relationship between things, and the rapid development of network science has also proved this. In order to measure the dynamic influence of music artists on the evolution of music, we used network science and technology to complete the following tasks related to musicians and music genres, and gave our conclusions on the evolution of music.

Firstly, We measure the influence of different musicians and genres through our self-built music network model. The musician is set as a node, and its influence on other musicians is taken as an edge, and three node indicators: degree, betweenness centrality and average clustering coefficient are selected to represent the musician’s "Music Influence" from different dimensions. Then, the characteristics of all the artists of the genre are used to represent the genre, and the influence between the genres is measured in the same way with artists.

Secondly, we built a similarity scoring system to analyze the similarities between musicians and genres. Through the R-type clustering of the 12 effective musical characteristics of musicians, we have obtained 5 indicators: Musicality, Key, Randomness, Track duration, Acoustics. We use the **TOPSIS** entropy method to construct a similarity measurement system, so that we can calculate the similarity score between the two according to the musician's music index. When using this system to evaluate the similarity between genres, in addition to giving a similarity matrix between the genres, we also further use the **Graph Kernel** method to more accurately measure the similarity between and within the genres from the perspective of the graph.

Thirdly, we built a music evolution model, focusing on the development of Pop/Rock music. Through multiple linear regression, we found that the Musicality indicator has the highest appeal in the influence process. At the same time, we established a **sliding window** to do **Moveout correlation analysis**, and obtained a highly related relationship between the two genres. In order to further illustrate the evolution process, we determined that Popularity is the music characteristic that can best measure the development of a genre, and then based on the inflection point detection to explore the time period when the Popularity of Pop/Rock changed the most as 1954-1964, 2000-2010, which is a major change. The Beatles and Rihanna are their representatives. Going deeper, we used dynamic time warping to find the dynamic influencer indicator of the genre as Acoustics, and we found that its changes are highly consistent with the changes in the popular genre.

Finally, we explored the development of Pop/Rock music from different angles, combined with the historical background, and found that it was more obviously affected by external changes. In addition, our work also demonstrates the cultural impact of music on society, and distinguishes the effects of different external influences on music. At the end of the paper, we submitted a one-page report to ICM.
