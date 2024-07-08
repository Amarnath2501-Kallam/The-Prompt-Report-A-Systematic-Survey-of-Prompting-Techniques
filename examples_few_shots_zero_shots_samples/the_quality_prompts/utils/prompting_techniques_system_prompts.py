from pydantic import BaseModel
from typing import List, Dict


class System2AttentionSystemPrompt(BaseModel):
    # Source: Page 4 of https://arxiv.org/pdf/2311.11829 -- only paragraph 1 of their prompt is used
    additional_information: str
    input_text: str

    @property
    def system_prompt(self) -> str:
        return f"""Given the following text by a user, extract the part that is unbiased and not their opinion,
    so that using that text alone would be good context for providing an unbiased answer to
    the question portion of the text.
    Text sent by User:
    {self.additional_information}
    """

    @property
    def messages(self) -> List[Dict[str, str]]:
        return [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {"role": "user", "content": self.input_text},
        ]


class SimtoMCharacterExtractionSystemPrompt(BaseModel):
    input_text: str

    @property
    def system_prompt(self) -> str:
        return """Which character's perspective is relevant to answer this user's question."""

    @property
    def messages(self) -> List[Dict[str, str]]:
        return [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {
                "role": "user",
                "content": self.input_text,
            },
        ]


class SimtoMSystemPrompt(BaseModel):
    # Source: Page 4 of https://arxiv.org/pdf/2311.10227
    additional_information: str
    character_name: str

    @property
    def system_prompt(self) -> str:
        return f"""The following is a sequence of events:
    {self.additional_information}
    Which events does {self.character_name} know about?"""

    @property
    def messages(self) -> List[Dict[str, str]]:
        return [
            {
                "role": "system",
                "content": self.system_prompt,
            },
        ]


class SelfAskSystemPrompt(BaseModel):
    # Source: Written by @sarthakrastogi
    input_text: str
    additional_information: str

    @property
    def system_prompt(self) -> str:
        return f"""Given the below information and the user's question, decide whether follow-up questions are required to answer the question.
    Only if follow-up questions are absolutely required before answering the present questions, return the questions as a Python list:
    # Example response:
    ["follow_up_question_1", "follow_up_question_2"]

    If the user's question can be answered without follow up questions, simply respond with "FALSE".

    # Provided information:
    {self.additional_information}"""

    @property
    def messages(self) -> List[Dict[str, str]]:
        return [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {
                "role": "user",
                "content": self.input_text,
            },
        ]


class StepBackPromptingSystemPrompt(BaseModel):
    # Source: Written by @sarthakrastogi
    input_text: str
    additional_information: str

    @property
    def system_prompt(self) -> str:
        return f"""Given the below information and the user's question, write a generic, high-level question about relevant concepts or facts that are required for answering the user's question.
    # Provided information:
    {self.additional_information}"""

    @property
    def messages(self) -> List[Dict[str, str]]:
        return [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {
                "role": "user",
                "content": self.input_text,
            },
        ]


class AnalogicalPromptingSystemPrompt(BaseModel):
    # Source: Improvised from page 5, section 5.1 of https://arxiv.org/pdf/2310.01714
    directive: str
    input_text: str
    output_formatting: str

    @property
    def updated_directive(self) -> str:
        return f"""{self.directive}
    When presented with a problem, recall relevant problems as examples. Afterward,
    proceed to solve the initial problem."""

    @property
    def updated_output_formatting(self) -> str:
        return f"""{self.output_formatting}
    # Problem:
    {self.input_text}
    # Instructions:
    ## Relevant Problems:
    Recall three examples of problems that are relevant to the initial problem. Your problems should be distinct from each other and from the initial problem. For each problem:
    - After "Q: ", describe the problem
    - After "A: ", explain the solution and provide the ultimate answer.
    ## Solve the Initial Problem:
    Q: Copy and paste the initial problem here.
    A: Explain the solution and provide the ultimate answer.
    """


class ThreadOfThoughtPromptingSystemPrompt(BaseModel):
    # Source: Page 4 of https://arxiv.org/pdf/2311.08734
    additional_information: str

    @property
    def context_summarisation_messages(self) -> str:
        context_summarisation_system_prompt = f"""{self.additional_information}
        Walk me through this context in manageable parts step by step, summarizing and analyzing as we go."""
        messages = [{"role": "system", "content": context_summarisation_system_prompt}]
        return messages


class TabularChainOfThoughtPrompingSystemPrompt(BaseModel):
    # Source: Written by @sarthakrastogi, output formatting taken from page 5, table 2 of https://arxiv.org/pdf/2305.17812
    directive: str
    input_text: str
    output_formatting: str

    @property
    def updated_directive(self) -> str:
        return f"""{self.directive}
        Think through the problem step by step to solve it.
        At each step, you have to figure out:
        - the step number,
        - the sub-question to be answered in that step,
        - the thought process of solving that step, and
        - the result of solving that step.
    """

    @property
    def updated_output_formatting(self) -> str:
        return f"""{self.output_formatting}
        Respond in the following markdown table format for each step:
        |step|subquestion|process|result|
    """
