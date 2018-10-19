# Zoho_Voice_Notifier
Python-based utility that notifies about newly added cases or answered cases in Zoho Desk

Structure:

    Task scheduler with task queue
    Zoho API based requestor of cases state
    GOOGLE API's reader of the titles
    Rcognizing of newly changed items or old ones to repeat it with different periods
    Integrated audio lib (for Win/Linux) for playing received from google data

I'm going to use CMD mp3 utility for windows from: https://lawlessguy.wordpress.com/2015/06/27/update-to-a-command-line-mp3-player-for-windows/