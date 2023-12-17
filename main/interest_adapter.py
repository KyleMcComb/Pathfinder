import re
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from database.models import Module, StudentInterest, Student
from django.core.exceptions import MultipleObjectsReturned

class InterestAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.awaiting_module_choice = False
        self.modules_to_choose = []
        self.student_id = 40191566  # using this id as a placeholder atm. - Will need to replace with student who is logged in.

    def can_process(self, statement):
        statement_text = statement.text.lower()
        return self.awaiting_module_choice or re.search(r'\b(like|dislike|hate)\b', statement_text) is not None

    def process(self, input_statement, additional_response_selection_parameters=None):
        statement_text = input_statement.text.lower()
        response = Statement('')

        if self.awaiting_module_choice:
            try:
                choice = int(statement_text)
                if 0 <= choice <= len(self.modules_to_choose):
                    if choice != 0:
                        module = self.modules_to_choose[choice - 1]
                        student = Student.objects.get(studentID=self.student_id)
                        try:
                            interest_obj = StudentInterest.objects.filter(studentID=student, interestName=module.moduleName).first()
                            if interest_obj:
                                interest_obj.interestImportance = 1
                                interest_obj.save()
                            else:
                                interest_obj = StudentInterest.objects.create(studentID=student, interestName=module.moduleName, interestImportance=1)
                                interest_obj.save()
                        except MultipleObjectsReturned:
                            interest_obj = StudentInterest.objects.filter(studentID=student, interestName=module.moduleName).first()
                            interest_obj.interestImportance = 1
                            interest_obj.save()
                        response.text = f"Thanks for your input! I've updated your interest for {module.moduleName}."
                    else:
                        response.text = "Thanks for your input! I will not update your interest for the given modules."
                else:
                    response.text = f"Sorry, you need to enter a number between 0 and {len(self.modules_to_choose)}."
            except ValueError:
                response.text = f"Sorry, you need to enter a number between 0 and {len(self.modules_to_choose)}."

            self.awaiting_module_choice = False
            self.modules_to_choose = []
        else:
            dislike_match = re.search(r'\b(dislike|do not like|don\'t like|dont like)\b', statement_text) # Can now tell difference between "I do not like, I don't like etc".
            hate_match = re.search(r'\bhate\b', statement_text)
            like_match = re.search(r'\blike\b', statement_text)

            if dislike_match:
                interest = statement_text[dislike_match.end():].strip()
                response_type = 'dislike'
            elif hate_match:
                interest = statement_text[hate_match.end():].strip()
                response_type = 'hate'
            elif like_match:
                interest = statement_text[like_match.end():].strip()
                response_type = 'like'

            try:
                student = Student.objects.get(studentID=self.student_id)
                modules = Module.objects.filter(moduleName__icontains=interest)
            except Student.DoesNotExist:
                response.text = "Sorry, you aren't currently logged in. So we can't update your interests for each module. Please log in to use full functionality."
                return response

            if response_type == 'like':
                if modules.count() >= 1:
                    response.text = f"That's great! Here are some modules related to {interest}:<br>"
                    for i, module in enumerate(modules, start=1):
                        response.text += f"{i}. {module.moduleID}: {module.moduleName}<br>"
                    response.text += f"Which one are you most interested in? Please enter the corresponding number or enter 0 if you are not interested in any."

                    self.awaiting_module_choice = True
                    self.modules_to_choose = list(modules)
                else:
                    response.text = f"You like {interest}. I will try and recommend any modules that contain {interest}."
            else:
                response.text = f"Thanks for providing me with this information. I won't recommend any modules that contain {interest}."

            response.confidence = 1
        return response