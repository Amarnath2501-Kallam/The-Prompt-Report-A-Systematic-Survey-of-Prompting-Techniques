# Write Quality Prompts

Use and evaluate prompting techniques quickly.

QualityPrompts implements 58 prompting techniques explained in [this survey from OpenAI, Microsoft, et al.](https://github.com/sarthakrastogi/quality-prompts/blob/main/README.MD#write-quality-prompts)

## 1. Install Quality Prompts:
```bash
pip install quality-prompts

2. Write the components of your prompt

from quality_prompts.prompt import QualityPrompt

directive = "You are given a document and your task..."
additional_information = "In the knowledge graph, ..."
output_formatting = "You will respond with a knowledge graph in..."

prompt = QualityPrompt(
    directive,
    additional_information,
    output_formatting,
    exemplar_store
)

3. QualityPrompts searches and uses only the few-shot examples that are relevant to the user's query

input_text = "List the disorders included in cvd"
prompt.few_shot(input_text=input_text, n_shots=1)

4. Simply call one of several prompting techniques to your prompt

System2Attention

Helps clarify the given context as an additional step before it's used to answer the question.

