# dyanye_clothing_era_classifier
An archeological survey of fashion from the 20th century to present

“D.Y.A.N.Y.E. - Dress your age (not your era)”: Clothing Era Classifier
Acknowledgement:
I’d like to acknowledge both Aaron Lichtner, data scientist with Nordstrom, and Jade Tabony, machine learning expert with MetaBrite, who helped me mold this idea from several others that I had been contemplating. Many others I have talked with have also given their inputs, in one way or another.


Business Understanding:
Question: Can you specify a clear research question, use case or business problem?

Response:
No one wants to dress badly. How can [we] help people to know if they are dressing in a modern, fashionable way that they choose, rather than staying in a slump? Perhaps a first step is to help people know which decade their style seems to fit most accurately. This may be a fun exercise for those who are “going for” a particular nostalgic/vintage look, but perhaps also a safeguard against dressing in a noticeably dated way.

Eventually (post-DSI), it would be ideal to have a mobile app with multiple ways to evaluate one’s clothing against a user-driven style guide, using feeds from one’s Tumblr/Pintrest/other social media. This could help users (or their loved ones) shop for items that “match” their existing style and also reference current trends that the user may wish to adopt.


Data Understanding:
Q: Can you specify potential data sources and includes a plan for obtaining data ?

R:
There are numerous ways of finding images that typify an era, which we’ll define here as a decade. To gain enough images to train a NN, I plan to use (open-source) digital art and fashion libraries, fashion catalogues (e.g. Sears, Nordstroms, JC Penny, which can be found in part or whole online).


Data Preparation:
Q: Can you include a conceptual explanation of the proposed data pipeline to transform raw data into an analytics base table (ABT) for modeling?

R: Phase 1 (for capstone-sensitive timeline)
Implement a web scrape images from multiple digital libraries, and online catalogue archives 
Compile images/pages in MongoDB in AWS S3 (for later analysis)
Implement a parser to label images belonging to a specific “era” 
Train a NN (Inception V3?) based on the labeled images for era classification
Use professionally procured costumes to a few distinct eras (e.g. 1920s, 1950s, 1980s, 2010s). (My cousin does this kind of thing for a living, though she has yet to commit to the idea.) If this is not feasible, I will perhaps take iconic (celebrities, advertisements, or similar) images of each of the eras, which “exemplify” an era. These will be my test data.
Create a web app that allows images to be uploaded and classified.


Modeling:
Q: Can you specify one or more specific statistical or machine learning techniques as candidates for evaluation ?

R: I think that KNN or hierarchical clustering may be most useful for the clustering of images. Though, as this project basically represents a form of a recommender system, I imagine that this next week in class will illuminate some other options/systems.


Evaluation:
Q: Can you devise a plan for evaluating model performance?

R: The ultimate goal of all this is to be able to classify images of one’s clothing choice and make a judgement, be it an “era” or something else (eventually a trend or personal style goal). If the system can learn what the features of that style are, perhaps by showing a histogram of “era” match percentage, or some other graphical interface. The point of the app is novelty and amusement around fashion/shopping. As it has been stated before, fashions and trend seem to be cyclical and, given enough user data, could become a serious tools for the “fashion layperson” to easily and quickly assess their clothing choices in a private, constructive way that could help retailers (i.e. Nordstrom) identify trends among their customers (past, present, and prospective).


Deployment:
Q: Can you specify a minimal viable product (MVP) for presentation and deployment?

R: At a minimum, the project needs to be able to classify user-driven images into an era. At first, this may mean that I use carefully chosen images as a proof-of-concept, with a few era-ambiguous choices to show that the system is evaluating based on what it “sees”.

