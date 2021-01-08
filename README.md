# imleagues-signup-bot
A selenium bot to automatically sign up for your desired session for services that use imleagues.com

Requires that chromium is installed and adblocker version 1.30.6_0

HOW TO USE:
1. Place the adblocker installation folder "1.30.6_0" in any directory and change path_to_adblocker to that path
2. Make sure PATH is correctly directed towards the chromedriver file of your chromium installation
3. Change the link inside the driver.get() function to the landing page of whichever imleagues application you are using
4. Change YOUR EMAIL and YOUR PASSWORD to your email and login respectively
5. For the fitness, dropdown, and times varibles, change the varibles to be clicked to the deisred activity, session, and time respectively
