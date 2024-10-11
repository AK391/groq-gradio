# `groq-gradio`

is a Python package that makes it very easy for developers to create machine learning apps that are powered by Groq's API.

# Installation

You can install `groq-gradio` directly using pip:

```bash
pip install groq-gradio
```

That's it! 

# Basic Usage

Just like if you were to use the `groq` API, you should first save your Groq API key to this environment variable:

```
export GROQ_API_KEY=<your token>
```

Then in a Python file, write:

```python
import gradio as gr
import groq_gradio

gr.load(
    name='llama-3.2-3b-preview',
    src=groq_gradio.registry,
).launch()
```

Run the Python file, and you should see a Gradio Interface connected to the model on Groq!

![ChatInterface](chatinterface.png)

# Customization 

Once you can create a Gradio UI from a Groq endpoint, you can customize it by setting your own input and output components, or any other arguments to `gr.Interface`. For example, the screenshot below was generated with:

```py
import gradio as gr
import groq_gradio

gr.load(
    name='llama-3.2-3b-preview',
    src=groq_gradio.registry,
    title='Groq-Gradio Integration',
    description="Chat with Llama 3.2 3B Preview model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()
```
![ChatInterface with customizations](groq-custom-gradio.png)

# Composition

Or use your loaded Interface within larger Gradio Web UIs, e.g.

```python
import gradio as gr
import groq_gradio

with gr.Blocks() as demo:
    with gr.Tab("Llama 3.2 3B Preview"):
        gr.load('llama-3.2-3b-preview', src=groq_gradio.registry)
    with gr.Tab("llama-3.2-1b-preview"):
        gr.load('llama-3.2-1b-preview', src=groq_gradio.registry)

demo.launch()
```

# Under the Hood

The `groq-gradio` Python library has two dependencies: `groq` and `gradio`. It defines a "registry" function `groq_gradio.registry`, which takes in a model name and returns a Gradio app.

# Supported Models in Groq

All chat API models supported by Groq are compatible with this integration. For a comprehensive list of available models and their specifications, please refer to the [Groq Models documentation](https://console.groq.com/docs/models).

-------

Note: if you are getting a 401 authentication error, then the Groq API Client is not able to get the API token from the environment variable. This happened to me as well, in which case save it in your Python session, like this:

```py
import os

os.environ["GROQ_API_KEY"] = ...
```
