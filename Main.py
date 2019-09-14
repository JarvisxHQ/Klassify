import lib.Topic as Topic
import lib.Sentiment as Sentiment

topic = Topic.getTopic(["Astronomers Find Water on an Exoplanet Twice the Size of Earth"])
sentiment = Sentiment.getSentiment(["Twenty years ago, almost to the day, two competing teams of astronomers independently discovered the first known transiting exoplanet—a world that, viewed from Earth, passed across the face of its star, casting a shadow toward watchful telescopes here. Two decades later, transits have become the lifeblood of exoplanet studies, yielding thousands of worlds via space telescopes such as NASA’s Kepler and Transiting Exoplanet Survey Satellite (TESS) missions and allowing researchers not only to gauge a planet’s size and orbit but also its density and bulk composition. In short, transiting worlds have proved to be the keystones in the burgeoning search for Earth’s cosmic twins. Back in 1999, however, the notion that these exoplanetary shadows would be detectable at all was so fantastic that validating it took the separate efforts of two groups."])
print(topic)
print(sentiment)