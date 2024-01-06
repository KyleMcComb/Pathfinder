import re
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from database.models import Module, StudentInterest, Student, Lecturer, Assessment, ModulePathway, Pathway
from django.core.exceptions import MultipleObjectsReturned
from database.models import Career
from django.db.models import Q

class InterestAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.awaiting_module_choice = False
        self.modules_to_choose = []
        self.student_id = 40191566  # using this id as a placeholder atm. - Will need to replace with student who is logged in.
        #self.student_id = None  # Initially set to None
        # studentInDb = Student.objects.get(studentID=request.user.username)

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
                        response.text = f"Thanks for your input! I've updated your interest for {module.moduleID} - {module.moduleName}."
                        careers_response = self.connect_careers_to_chatbot(interest=None, module=module)
                        response.text += careers_response
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
                modules = Module.objects.filter(
                    Q(moduleName__icontains=interest) | Q(moduleDescription__icontains=interest) |
                    Q(moduleID__iexact=interest) #iexact  - used to check if an item matches case-insensitiviely 
                )
            except Student.DoesNotExist:
                response.text = "Sorry, you aren't currently logged in. So we can't update your interests for each module. Please log in to use full functionality."
                return response

            if response_type == 'like':
                if modules.count() >= 1:
                    response.text = f"That's great! Here are some modules related to {interest}:<br><br>"
                    for i, module in enumerate(modules, start=1):
                        response.text += f"{i}. {module.moduleID}: {module.moduleName}<br>"
                        response.text += f"Module Description: {module.moduleDescription}<br> Module Level: {module.moduleLevel}<br> Module Weight: {module.moduleWeight}<br>"
                        # Query for lecturers associated with this module
                        lecturers = Lecturer.objects.filter(lecturerModules=module)
                        lecturer_names = ', '.join([lecturer.lecturerName for lecturer in lecturers])
                        response.text += f"Lecturers: {lecturer_names if lecturer_names else 'Not available'}<br>"
                        # Fetch and format assessments
                        assessments = Assessment.objects.filter(moduleID=module)
                        if assessments:
                            for assessment in assessments:
                                response.text += f"Assessment: {assessment.assessmentType}, Weight: {assessment.assessmentWeight}%<br>"
                        else:
                                response.text += "Assessments: Not available<br>"

                        if module.moduleSemester == 3:
                            response.text += f"Module Semester: Module takes place over both semesters<br>" 
                        else:
                            response.text += f"Module Semester: {module.moduleSemester}<br>"

                        # Fetch and format pathways
                        module_pathways = ModulePathway.objects.filter(moduleID=module)
                        pathways = [Pathway.objects.get(pathwayID=mp.pathwayID).pathwayName for mp in module_pathways]
                        pathways_text = ", ".join(pathways) if pathways else "Not available"
                        response.text += f"Pathways: {pathways_text}<br><br>"
                    response.text += f"Which one are you most interested in? Please enter the corresponding number or enter 0 if you are not interested in any.<br>"

                    self.awaiting_module_choice = True
                    self.modules_to_choose = list(modules)
                else:
                    careers_response = self.connect_careers_to_chatbot(interest=interest, module=None)
                    response.text = f"You like {interest}. I will try and recommend any modules that contain {interest}."
                    response.text += careers_response
            else:
                response.text = f"Thanks for providing me with this information. I won't recommend any modules that contain {interest}."

            response.confidence = 1
        return response

    
    def find_percent_of_careers_related(self, interest=None, module=None):
        if interest:
            query_filter = Q(jobDescription__icontains=interest) | Q(jobTitle__icontains=interest)
            relevant_careers = Career.objects.filter(query_filter)
        elif module:
            relevant_careers = module.careers.all()  # Accessing related careers directly from the module
        else:
            return 0, []

        all_careers_count = Career.objects.count()
        relevant_careers_count = relevant_careers.count()
        percent_of_relevant_careers = (relevant_careers_count / all_careers_count) * 100 if all_careers_count else 0
        relevant_career_titles = [career.jobTitle for career in relevant_careers]

        return percent_of_relevant_careers, relevant_career_titles
    
    
    def connect_careers_to_chatbot(self, interest, module):
        # Check which parameter is provided and call the appropriate method
        if module is not None:
            percent_of_relevant_careers, relevant_career_titles = self.find_percent_of_careers_related(module=module)
            context = f"module {module.moduleName}"
        elif interest is not None:
            percent_of_relevant_careers, relevant_career_titles = self.find_percent_of_careers_related(interest=interest)
            context = f"interest ({interest})"
        else:
            return "No specific career suggestions can be provided without interest or module information."

        # Remove duplicates by converting the list to a set, then back to a list
        unique_career_titles = list(set(relevant_career_titles))

        # Join the job titles with a comma
        relevant_career_titles_str = ", ".join(unique_career_titles)
        careers_response = f"<br><br>Your {context} was found to be relevant in {percent_of_relevant_careers:.2f}% of IT job roles we've checked."
        
        if relevant_career_titles_str:
            careers_response += "<br>Here are some of the relevant job roles we have found:<br>"
            for career_title in unique_career_titles:
                careers_response += f"- {career_title}<br>"
        else:
            careers_response += f"<br>We found no specific IT career suggestions for {context}."

        return careers_response