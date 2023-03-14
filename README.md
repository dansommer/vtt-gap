# VTT Gap finder

This project attempts to identify potential places for Audio Description narration by using a VTT file containing the dialogue. 

The user inputs:

1) VTT file 
2) Output file name 
3) Minimum gap duration to detect

The script will generate either of both of the following

1) Original & AD Potentials - VTT with the original dialogue and new captions frames with the text "AD possibility"
2) AD Potentials Only - Only caption frames with "AD possibility" (no original dialogue). 

Python / Flask application created with the help of ChatGPT.

Demo: https://dansome.pythonanywhere.com/

See exchange with ChatGPT here - https://sharegpt.com/c/YS3H8gw
It wasn't a straight shot, but considering I'm not a developer, this wasn't a bad way to spend two hours. 
