# CodeSamples
This is a repository of code that I have written traveling a life long path of improving my programming skills.  I worked each problem out by myself; I have not copied other peoples work.  Most of the samples are answers to questions in educational books.  There is also a set of solutions to problems that I found interesting and wanted to work through via code.  Where appropriate, in a file, I will add a brief description of important thoughts that were key to the process.  When I have to reference external information I will note that as well.  If I solve a problem in multiple languages the file name will be the same but the file extension will reflect the language.  Below is a rough index and naming convention for the files in this directory.

# Books
1. "Cracking the Coding Interview" by Gayle Laakmann McDowell.
   Files are named ctci-chapterNumber-questionNumber.

# Interesting Problems 
1.  haversine_UDF.js
    This file is actually a PostgreSQL UDF written in python then converted to javascript.  It returns a haversine value given two lat/lon degree coordinates from within the database.  The result is used to order the SQL results.
2.  aspect_UDF.js
    This file is actually a PostgreSQL UDF written in python then converted to javascript.  It returns a boolean stating whether two astronomical bodies are with a certain degree range of one another on the elliptic as viewed from Earth.
