import re
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from database.models import Module

class YearAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        statement_text = statement.text.lower()
        return re.search(r"\b(?:first year|second year|final year|fourth year|1st year|2nd year|3rd year|4th year|year 1|year 2|year 3|year 4|stage 1|stage 2|stage 3)\b", statement_text) is not None

    def process(self, input_statement, additional_response_selection_parameters=None):
        statement_text = input_statement.text.lower()
        response = Statement("")

        year_match = re.search(r"\b(?:first year|second year|final year|fourth year|1st year|2nd year|3rd year|4th year|year 1|year 2|year 3|year 4|stage 1|stage 2|stage 3)\b", statement_text)
        if year_match:
            year = year_match.group()

        if year in ["first year", "1st year", "year 1", "stage 1"]:
            first_year_modules = Module.objects.filter(moduleID__startswith="CSC1")
            response.text = "Good to know. Here are all the first-year modules you can do for EEECS:<br>"
            for module in first_year_modules:
                response.text += f"- {module.moduleID}: {module.moduleName}<br>"
        elif year in ["second year", "2nd year", "year 2", "stage 2"]:
            second_year_modules = Module.objects.filter(moduleID__startswith="CSC2")
            response.text = "Good to know. Here are all the second-year modules you can do for EEECS:<br>"
            for module in second_year_modules:
                response.text += f"- {module.moduleID}: {module.moduleName}<br>"
        elif year in ["final year", "3rd year", "year 3", "stage 3"]:
            final_year_modules = Module.objects.filter(moduleID__startswith="CSC3")
            response.text = "Good to know. Here are all the final year modules you can do for EEECS:<br>"
            for module in final_year_modules:
                response.text += f"- {module.moduleID}: {module.moduleName}<br>"
        elif year in ["fourth year", "4th year", "year 4", "stage 4"]:
            fourth_year_modules = Module.objects.filter(moduleID__startswith="CSC3")
            response.text = "Good to know. Here are all the fourth-year modules you can do for EEECS:<br>"
            for module in fourth_year_modules:
                response.text += f"- {module.moduleID}: {module.moduleName}<br>"

        response.confidence = 1
        return response