<h1>How Twitter Popular are you?</h1>
<h4>Hosted at sravantitekumalla.appspot.com </h4>
<br>
<h4> The name says it all. Put in your twitter handle (or anyone else’s) and discover how popular they are on Twitter. </h4>
<br>

<h2> Current implementation </h2>
<p> This web app is run using Goole App Engine, Python and tweepy to access the Twitter API. 
User stats are accessed based on their twitter handle, including: 
<ul>
<li> Number of followers </li>
<li> Number following </li>
<li> Number of mentions (more tricky to do, so I ended up doing a search with their username as the query) </li>
<li> For each tweet, the number of times it’s been RT’ed and favorited </li>
</ul>

Using this data, the follower/following ratio is calculated, the average favorites/tweet, RTs/tweet, and then the popularity is determined by multiplying the numbers by 10 and adding them. Obviously this isn’t the final algorithm and I will scale it. 
</p>
<br>

<h2> Current Goals and Bugs </h2>
<p> This is only the first version, so there are a lot of things I’m going to work on this week and next, which include: 
<ul>
<li> Handling exceptions when the twitter handle doesn’t exist, when there are 0 tweets (because you can’t divide by 0 tweets for averages, 0 following, etc)</li>
<li> Figuring out pagination using tweepy so I get more than 200 tweets (the max Twitter API allows is 800) </li>
<li> The RTs don’t account for <i> who </i> retweeted the tweet, so if you retweeted something from a popular/credible person on twitter who gets 1000s of RTs, your average shoots up, which isn’t accurate. Still working on finding a way to get only the people who RT <i> your </i> RT. </li>
<li> Fixing the size of the “@“ in the entry bar </li>
</ul>