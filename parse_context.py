"""
Author: Radu Vasilescu
Date:   2020-11-10
"""

import os
import sys
import openai

"""
Determines the input method for the script. 

A value of True reads the program's input from the command line interactively.
A value of False reads the program's input from the process' STDIN. An example of 
non-interactive usage is:

    cat ./conversations/dinner.txt | python3 parse_content.py
"""
INTERACTIVE : bool = False

openai.api_key : str = os.environ["OPENAI_API_KEY"]

# Set up 4-shot example prompts:
examples : str = "The following is a list of conversations between humans. A voice-activated AI suggests information that might be relevant in the context of the conversation.\n\nA: I'm going to leave for work soon.\nB: Okay, I'm leaving too.\nA: Let me get dressed first.\nContext: Two people are about to leave for work.\nUseful Output: Current weather, current traffic, estimated commute time, reminders\nRelevant Data Sources: Query Google Weather API to get current weather, query Google Maps API to get traffic and commute time, query Reminders app to get reminders.\n\nA: Have you seen that movie, Avengers Endgame?\nB: Oh, yeah! I saw it when it came out. I loved Iron Man in that series!\nA: Who played him again? \nB: I don't remember.\nContext: Two people are wondering who played Iron Man in the film Avengers Endgame\nUseful Output: Robert Downey Jr.\nRelevant Data Sources: Query Google Search for \"Who plays Iron Man in Avengers Endgame?\"\n\nA: So, when do you guys want to meet up later?\nB: I don't know, I have a pretty busy evening\nC: I'm free after 5:00pm\nA: Let me look at my schedule.\nContext: A group of people is trying to schedule an event this evening.\nUseful Output: Today's remaining calendar events.\nRelevant Data Sources: Query Google Calendar API for events after 5pm today.\n\nA: I have to pick my daughter up from school today.\nB: Okay, what time is that going to be?\nContext: Two people are talking about a plan to pick someone up from school\nUseful Output: Reminder to pick up the child, current traffic conditions to the school, estimated time to the school\nRelevant Data Sources: Add a reminder to the Reminders app, query Google Maps API for current traffic and school location, query Google Maps API for estimated travel time\n\n"

start_sequence : str = "Context:"

conversation : str = ""
if INTERACTIVE:
    # Read the conversation from the console
    print('Enter conversation. Use /end to signal the end.\n')

    while (line := input()) != '/end':
        conversation += line + "\n"
else:
    # Read the conversation from standard input
    for line in sys.stdin:
        if line == "\n" or line == "/end":
            print("Do not include neither newlines nor /end in the input (INTERACTIVE = %s)", str(INTERACTIVE))
            exit(1)
        conversation += line

print('Generating completion...')

response = openai.Completion.create(
  engine = "davinci",
  prompt = examples + conversation + start_sequence,
  temperature = 0.7,
  max_tokens = 64,
  top_p = 1,
  stop = ["\n\n"]
)

response_text : str = response["choices"][0]["text"]
response_split = response_text.split("\n")
gen_context, gen_output, gen_sources = response_split[0].strip(), response_split[1].strip(), response_split[2].strip()

print('Context: ' + gen_context)
print(gen_output)
print(gen_sources)
