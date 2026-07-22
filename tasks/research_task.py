import textwrap

from crewai import Task
from agents.research_specialist import research_specialist_agent


research_task = Task(
    agent=research_specialist_agent,
    description=textwrap.dedent("""
        Research the topic: {topic}

        Provide:
        - Short introduction
        - 5 key findings
        - Recent developments
        - Conclusion

        Keep the answer concise.
    """),
    expected_output="A concise research summary",
    output_file="research_findings.md"
)