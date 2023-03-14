# VTT Gap finder

This tool identifies potential places for Audio Description narration by using a VTT file containing the dialogue and user input. 

The user provides:

1) VTT file with dialogue (subtitles) or closed captions (SDH - subtitles for deaf and hard of hearing)
2) Output file name (whatever you want)
3) Minimum gap duration to detect
4) Desired VTT output(s) (see below)

The script will generate either of both of the following:

1) Original & AD Potentials - VTT with the original dialogue and new captions frames with the text "AD possibility"
2) AD Potentials Only - Only caption frames with "AD possibility" (no original dialogue). 

<b>Potential Uses </b><br>
1) This could be used as a tool to quickly assess if there are enough pauses in the video to consider Standard Audio Description (WCAG 2.1 Sucess Criteria 1.2.5) or if further examination is needed to assess if Extended Audio Description ((WCAG 2.1 Sucess Criteria 1.2.7) is necessary. 
2) Reduce time in Audio Description production workflows.

Python / Flask application created with the help of ChatGPT.

Demo: https://dansome.pythonanywhere.com/

See exchange with ChatGPT here - https://sharegpt.com/c/YS3H8gw
It wasn't a straight shot, but considering I'm not a developer, this wasn't a bad way to spend two hours. 
