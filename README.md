# jovian-careers-website
A careers website for Jovian

## Things to deal with in the before future enhancement:
Currently I'm using fstring to specify the database conn settings, but this is not correct because the repository is public and If I'm was'nt use a local mysql db, Every body could see the conn settings and connect to the database...
For that I stored the sensitive information in a python file to use it like a module, also I add this file (DBconf.py) to the .gitignore to prevent it from getting followed by git.
But the best abroach is to use the environemet variables .env file to store the sensitive data, and  with the os module and the help of os.get_env() we use this data as we want, without forgetting to add the .env to the .gitignore file (added by default)

I've create a webpage that confirm the application to the user, but i hav to send the application information to the database, I've allready create the application table in the data base, but I'v struguled with inserting the data to it, I tried to figure it out but it still did'nt work as expected, I will leave the code as comment, and maybe in the near future, I will look at it.

the tutorial vedio in the spesific time to continue working: https://youtu.be/yBDHkveJUf4?t=15996

## Future Enhancement:
1. send an email to admin and candidate on application submission
2. Use captcha in hte application form to prevent spam/bots
3. Create an admin login interface to check submitted applications
4. Allow admins to mark applications as accepted/rejected
5. Create a user login interface to check application status
