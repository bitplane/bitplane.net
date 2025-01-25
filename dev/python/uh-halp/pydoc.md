<a id="uh_halp"></a>

# uh\_halp

<a id="uh_halp.backend.openai"></a>

# uh\_halp.backend.openai

For calling the OpenAI completion model.

<a id="uh_halp.backend.openai.query"></a>

#### query

```python
def query(model: str, system_prompt: str, user_prompt: str, key: str) -> str
```

Calls the OpenAI API with the query from the command line.

<a id="uh_halp.backend"></a>

# uh\_halp.backend

<a id="uh_halp.backend.web_api"></a>

# uh\_halp.backend.web\_api

Generic web API functions

<a id="uh_halp.backend.web_api.query"></a>

#### query

```python
def query(endpoint: str, method: str, query: str, post_data: str,
          headers: dict[str, str], response_path: list[str | int]) -> str
```

Standard web API request.

<a id="uh_halp.backend.web_api.extract"></a>

#### extract

```python
def extract(response: requests.Response,
            response_path: list[str | int]) -> str
```

If there's a response_path list, treat the response as JSON and the list as
the path to the key we want. Use strings for property names, ints for list
indices, and you can use negative indices to reference the end of a list
(i.e. -1 for the last item.)

<a id="uh_halp.backend.util"></a>

# uh\_halp.backend.util

<a id="uh_halp.backend.util.clean"></a>

#### clean

```python
def clean(response: str) -> str
```

Cleans the response from the API, because we can't trust it to play nicely.

<a id="uh_halp.keys"></a>

# uh\_halp.keys

<a id="uh_halp.keys.prompt_key"></a>

#### prompt\_key

```python
def prompt_key(service: str) -> str
```

Prompt the user for a key for the given service, returning it as a string

<a id="uh_halp.keys.load_keys"></a>

#### load\_keys

```python
def load_keys(key_file: str = KEY_FILE) -> dict[str, str]
```

Load the keys from disk and return them

<a id="uh_halp.keys.save_keys"></a>

#### save\_keys

```python
def save_keys(keys: dict, key_file: str = KEY_FILE)
```

Save all the keys to disk

<a id="uh_halp.keys.save_key"></a>

#### save\_key

```python
def save_key(service: str, key: str, key_file: str = KEY_FILE)
```

Save the service's key to disk

<a id="uh_halp.keys.load_key"></a>

#### load\_key

```python
def load_key(service: str, key_file: str = KEY_FILE) -> str | None
```

Load the key from disk, returning it.

<a id="uh_halp.keys.get_key"></a>

#### get\_key

```python
def get_key(service: str) -> str
```

Loads the service's key from ~/.uh-keys, or prompts for it and saves it there.

<a id="uh_halp.config"></a>

# uh\_halp.config

<a id="uh_halp.config.reset_config"></a>

#### reset\_config

```python
def reset_config(path: str = CONFIG_FILE)
```

Resets the config file to the template

<a id="uh_halp.config.save_config"></a>

#### save\_config

```python
def save_config(config, path: str = CONFIG_FILE)
```

Saves the config file

<a id="uh_halp.config.get_config"></a>

#### get\_config

```python
def get_config(path: str = CONFIG_FILE)
```

Reads the config file, creating it from template if it doesn't exist

<a id="uh_halp.vars"></a>

# uh\_halp.vars

Gets template variables that can be inserted into the context.

<a id="uh_halp.vars.get_os"></a>

#### get\_os

```python
def get_os() -> str
```

Returns a string describing the OS.

<a id="uh_halp.vars.get_shell"></a>

#### get\_shell

```python
def get_shell() -> str
```

Returns the user's shell executable name.

<a id="uh_halp.vars.apply_vars"></a>

#### apply\_vars

```python
def apply_vars(vars: dict, template: Any) -> Any
```

Replaces strings in a json-style object tree. Use {var}

<a id="uh_halp.vars.get_vars"></a>

#### get\_vars

```python
def get_vars() -> dict
```

Gets variables that can be replaced with templates.
To use one, reference it like {var} in any string field.

Current keys are:

- shell: The user's shell executable name.
- os: A string describing the OS and its version.
- query: The query string.
- pwd: The current working directory.
- key: the secret key for the service (blank here, requested interactively if needed)

<a id="uh_halp.main"></a>

# uh\_halp.main

Contains main entrypoint

<a id="uh_halp.main.show_help"></a>

#### show\_help

```python
def show_help()
```

uh
command line help on the command line

Usage: uh [query]

**Example**:

  user@host$ uh get the time
  date +%H:%M:%S

  config is in ~/.uh_config. Each field is parsed with mustache.
  Access tokens go in ~/.uh-keys

<a id="uh_halp.main.get_func"></a>

#### get\_func

```python
def get_func(module_name: str, func_name="query") -> Callable
```

Returns a function in the given module name.

<a id="uh_halp.main.main"></a>

#### main

```python
def main() -> int
```

Entrypoint for the CLI.

<a id="uh_halp.__main__"></a>

# uh\_halp.\_\_main\_\_

