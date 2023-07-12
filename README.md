# scraping_dojo_07_2023

**Task Description**
Implement a program that automatically scrapes all quotes (from all next pages) from the xxx website and saves them to a single jsonl (JSON Lines) file upon execution. Note: The program should scrape the website xxx where the text appears with a random delay of a few seconds. Substituting this page will result in disqualification.

**Definitions of Done**
1. The project is implemented in Python. Dependencies should be installed by executing the command pip install -r requirements.txt
2. The scraping process should be started by the command python run.py without any parameters.
3. All parameters - proxy, name of the output file, and input URL to be scraped should be placed in the .env
file. This file (.env) should NOT be pushed into a repository. If the .env file is located inside a repository or any of the parameters listed below are hardcoded, the task will not be reviewed.
4. Upon completion, the process should save the output.jsonl file in the same base location as the run.py file.
5. Each line of the output.jsonl file should be in JSON format, with the following fields:
{
    "text": "The world as we have created it is a process of our thinking. It cannot be changed
without changing our thinking",
    "by": "Albert Einstein",
    "tags": ["change", "deep-thoughts", "thinking", "world"]
}


**Evaluation Criteria / How to Get the Most Points**
1. Use modularity and object-oriented code, correctly defining objects, their properties, and methods.
2. Write clean code and use correct function and object method names.
3. Use delivered proxy for scraping in a proper way (from .env file). If the proxy does not work, you can
choose not to use it.
4. Ensure the reliability of the scraping solution by closely imitating browser behavior. (When scraping, there are different methods to choose from. It is generally preferred to use the ones that mimic browser behavior.)
5. Generate output file with correct results (Note: There are several pages of quotes, you should scrape them all)

