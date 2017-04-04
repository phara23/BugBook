# BugBook
An extremely simple command line tool for bug tracking that seeks to help programmers avoid the headache of solving the same bug twice.

This CL tool comes with two basic commands: add & search.

add is used to write bugs and their solutions to a local file while search is used to query these existing stored bugs and solutions, looking for bugs similar to the one provided to the search command. 

The add command can be invoked like so at the terminal:

python bugbook.py add "bugTitle" "bugType" "techInvolved" "bugNotes" "solutionNotes"

an example is shown below:

python bugbook.py add "UI is updated very slow in swift" "UI bug" "swift xcode" "this is very weird. it seems like updates to the UI are either just not happening or are happening very delayed." "If the UI is updated on a background thread it will suffer a big delay. Force things to be on the main thread if they are UI related and are currently not on the main thread."

The search command can be invoked like so at the terminal:

python bugbook.py search "bugType" "techInvolved" "problemNotes"

an example is:

python bugbook.py search "run time crash" "xcode swift" "lots of anal and the app crashes with message asking me to check my anus"
