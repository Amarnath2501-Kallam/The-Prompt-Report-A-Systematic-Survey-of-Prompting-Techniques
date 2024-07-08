# Write Quality Prompts

Use and evaluate prompting techniques quickly.

QualityPrompts implements 58 prompting techniques explained in [this survey from OpenAI, Microsoft, et al.](https://github.com/sarthakrastogi/quality-prompts/blob/main/README.MD#write-quality-prompts)

## 1. Install Quality Prompts:
```bash
pip install quality-prompts

## 2. Write the components of your prompt
```bash
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

