import bin.Article as Article
import bin.Tweets as Tweets
import bin.Chats as Chats
import bin.News as News
import bin.Email as Email

#title = ["Astronomers Find Water on an Exoplanet Twice the Size of Earth"]
#data = ["Twenty years ago, almost to the day, two competing teams of astronomers independently discovered the first known transiting exoplanet—a world that, viewed from Earth, passed across the face of its star, casting a shadow toward watchful telescopes here. Two decades later, transits have become the lifeblood of exoplanet studies, yielding thousands of worlds via space telescopes such as NASA’s Kepler and Transiting Exoplanet Survey Satellite (TESS) missions and allowing researchers not only to gauge a planet’s size and orbit but also its density and bulk composition. In short, transiting worlds have proved to be the keystones in the burgeoning search for Earth’s cosmic twins. Back in 1999, however, the notion that these exoplanetary shadows would be detectable at all was so fantastic that validating it took the separate efforts of two groups."]
#Article.classifyArticle(title, data)

#tweet = ["Congratulations to #StarTrekDiscovery on their #SaturnAward win for Best Streaming Science Fiction, Action & Fantasy Series #StarTrekFamily"]
#Tweet.classifyTweet(tweet)

#text = ["Do you want grab a coffee?"]
#Chats.classifyChat(text)

#title = ["Today’s your last chance to get the Borderlands 3 preorder deal for PS4 and Xbox"]
#data = ["There’s no question whatsoever that Borderlands 3 is one of the most hotly anticipated new games of the season. In fact, with just one day left until it’s released, Borderlands 3 is currently the best-selling title on both PlayStation 4 and Xbox One. Oh, and guess what the #2 best-selling game is. That’s right… it’s Borderlands 3 Super Deluxe Edition! Everyone’s going to be talking about this game over the coming weekend following its release, and you definitely don’t want to be left out. If that’s not enough incentive, today is your last chance to take advantage of Amazon’s awesome deal for Prime members that saves you $10 when you preorder! Hurry though, because this deal vanished at the end of the day on Thursday since Borderlands 3 is set to be released tomorrow."]
#News.classifyNews(title, data)

email = ["From: Coursera <no-reply@m.mail.coursera.org>\n Subject: The 12 Most Popular Data Science Courses on Coursera\n [ Courses Our Learners Love ... ]\nThe 12 Most Popular Data Science Courses on Coursera\n[Courses]\nBuild career skills in as little as a few hours with online courses that \nlearners love. Find your #CourseToSuccess with the world’s best \nuniversities and companies.\n________________________________\n[ML]\nMachine Learning\nStanford University\nEnroll Now\n[DS]\nWhat is Data Science?\nIBM\nEnroll Now\n[Neural Network]\nNeural Networks and Deep Learning\ndeeplearning.ai\nEnroll Now\n[DS Python]\nIntroduction to Data Science in Python\nUniversity of Michigan\nEnroll Now\n[Tools]\nThe Data Scientist’s Toolbox\nJohns Hopkins University\nEnroll Now\n[Data]\nSQL for Data Science\nUniversity of California, Davis\nEnroll Now\n[Math]\nMathematics for Machine Learning: Linear Algebra\nImperial College London\nEnroll Now\n[GCP]\nGoogle Cloud Platform Big Data and Machine Learning Fundamentals\nGoogle Cloud\nEnroll Now\n[Probability]\nIntroduction to Probability and Data\nDuke University\nEnroll Now\n[ML]\nHow Google does Machine Learning\nGoogle Cloud\nEnroll Now\n[Big Data]\nIntroduction to Big Data\nUniversity of California San Diego\nEnroll Now\n[Decision Making]\nData-driven Decision Making\nPricewaterhouseCoopers\nEnroll Now\nExplore more courses\nExplore\nValentine’s Day courses, just for you!\nHappy Valentine’s Day! We wish you a lifetime filled with love and \nlearning. To celebrate, we’ve made you a list of 10 courses and \nSpecializations about love, emotion, and self-care.\n[Valentines]\n[FB]\n[Twitter]\n[LI]\n[iOS]\n[Android]\nLearner Help Center\n| Privacy Policy\n| Email Settings\n| Unsubscribe\n© 2019 Coursera | 3﻿81 E. E﻿velyn A﻿ve, M﻿ountain V﻿iew, C﻿A 9﻿4041 U﻿SA"]
Email.classifyEmail(email)