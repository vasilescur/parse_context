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
- OpenAI API key (currently in private beta)

### Installation

#### API Key Setup

First, set up your API key:

```bash
export OPENAI_API_KEY='sk-<your key here>'
```

To make it persistent,

```bash
echo "export OPENAI_API_KEY='sk-<your key here>'" >> ~/.bashrc && source ~/.bashrc
```

#### Python and Packages Setup

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

### License

This is released under the MIT License.

### Legal

Please refer to the OpenAI website for information regarding the legal and copyright status of content produced by GPT-3.
By using this software, you agree that as the repository author, Radu Vasilescu, I am not responsible for any content
produced by this software, including completions and model output. All content/media produced with this software must
be attributed to the person or company who produced the output-- not me, and not OpenAI.
