# `parse_context`

This program uses the OpenAI API, powered by GPT-3, to power the logic of a context-based
active-listening voice assistant. The context of this software is:

- Humans have a conversation, which is recorded and transcribed in real time.
- (**THIS PROGRAM**) The conversation is sent to the OpenAI API along with a few-shot list of examples. The API returns a 
detected context, suggestions for what outputs would be useful to the humans, and a list of data sources 
for achieving those outputs.
- The voice assistant presents the data to the user to augment the conversation.

## Requirements

- Python 3
- OpenAI Python Client

### Installation

Install Python. Install Pip for Python3. Then run:

```bash
pip3 install -r ./requirements.txt
```

To update the requirements file after changing, you can use:

```bash
pip3 freeze > ./requirements.txt
```

Or

```bash
pip3 freeze | grep openai > ./requirements.txt
```

## Usage

### Interactive Mode

To use interactive mode, make sure the `INTERACTIVE` flag at the top of `parse_context.py` is set to `True`.

Then, run `python3 parse_context.py`. You can enter the conversation on the command line
in the following format, using `/end` to stop.

```
A: Hey, what tech stack do you think we should use for the new app?
B: What app?
A: The dating app we are developing. It needs to be cross-platform mobile.
B: Oh, okay. Um... I don't really know any good frameworks
/end
```

The result will be printed to `STDOUT` (default is the terminal window).

### Non-interactive mode

To use non-interactive mode, make sure the `INTERACTIVE` flag at the top of `parse_context.py` is set to `False`.

Then, run the program while passing your conversation to standard input (`STDIN`). For example, if the above
conversation were placed in a file located at `./conversations/tech_stack.txt`, we could run:

```bash
cat ./conversations/tech_stack.txt | python3 parse_context.py
```

And the result will be printed to `STDOUT`.