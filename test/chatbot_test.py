import unittest
from main.chatbot_settings import *
from main.chatbot import *
# Create your tests here.

#python Pathfinder/manage.py test Pathfinder.test.chatbot_test

class ChatbotTestCase(unittest.TestCase):

    
    def test_hate_response(self): 
        message = "I hate maths"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "Thanks for providing me with this information. I won't recommend any modules that contain maths.")

    # Chatbot identifies the input as having a negative sentient towards maths

    def test_unrelated_response(self):
        message = "What time is it?"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "I am sorry, but I do not understand.")


    def test_invalid_response(self):
        message = "hdfjkahfda"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "I'm sorry but I can only take valid input as a response.")
        # Planned fail as chatbot doesn't recognise if the input is just random characters

    def test_incorrect_language_response(self):
        message = "Bonjour"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "I'm sorry but I can only take responses that are in English," 
                         + "here is the contact information for the student support office that may be able to help you: <email>")
        # Planned fail as chatbot can not identify the language given and respond with the appropriate error message in that language. 

    def test_user_interest_response(self):
        message = "I like maths"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "That's great! Here are some modules related to maths:<br>1. CSC1026: Fundamentals of Maths for Computing<br>" + 
                         "Which one are you most interested in? Please enter the corresponding number or enter 0 if you are not interested in any.")
    
    def test_unknown_interest_response(self):
        message = "I like history"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "You like history. I will try and recommend any modules that contain history.")

    def test_user_academic_records_response(self):
        message = "I have taken a lot of math courses"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "That's great! Here are some modules related to maths:<br>1. CSC1026: Fundamentals of Maths for Computing<br>" + 
                         "Which one are you most interested in? Please enter the corresponding number or enter 0 if you are not interested in any.")
        # Planned fail as chatbot doesn't recognise input of academic records yet.


    def test_stage_1(self):
        message = "List modules for stage 1"
        response = str(chatbot.get_response(message)) 
        self.assertEqual(response, "Good to know. Here are all the first-year modules you can do for EEECS:<br>- CSC1023: Databases<br>- CSC1024: Programming and Systems Development<br>"
                         + "- CSC1025: Procedural Programming<br>- CSC1026: Fundamentals of Maths for Computing<br>- CSC1027: Programming<br>- CSC1028: Computer Science Challenges<br>"
                         + "- CSC1029: Object Oriented Programming<br>- CSC1030: Web Technologies<br>- CSC1031: Introduction to Cyber Security<br>"
                         + "- CSC1033: Introduction to Computer Architecture<br>- CSC1032: Introduction to Cyber Security<br>")
        
    def test_stage_2(self):
        message = "List modules for stage 2"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "Good to know. Here are all the second-year modules you can do for EEECS:<br>- CSC2051: Systems Administration and Supoort<br>- CSC2052: Server Side Web Development<br>"
                         + "- CSC2053: Intoduction to Enterprise Computing<br>- CSC2054: User Experience Design<br>- CSC2056: Systems Security and Cryptography<br>- CSC2057: Modern Web App Development<br>"
                         + "- CSC2058: Software Engineering and Systems Development<br>- CSC2059: Data Structures and Algorithms<br>- CSC2060: Theory of Computation<br>"
                         + "- CSC2062: Introduction to AI and Machine Learning<br>- CSC2063: Service Oriented Programming<br>- CSC2065: Professional and Transferrable Skills<br>- CSC2066: Networks and Protocols<br>")


    def test_stage_3(self):
        message = "List modules for stage 3"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "Good to know. Here are all the final year modules you can do for EEECS:<br>- CSC3001: Formal Methods<br>- CSC3002: Computer Science Project<br>- CSC3021: Concurrent Programming<br>"
                         + "- CSC3023: BIT Project<br>- CSC3031: Software Design Principles and Patterns<br>- CSC3032: Software Engineering Project<br>- CSC3045: Contemporary Team-Based Projects<br>"
                         + "- CSC3047: CIT Project<br>- CSC3056: Software Testing<br>- CSC3058: Advanced Computer Architectures/Systems<br>- CSC3059: Malware Analysis<br>"
                         + "- CSC3062: Data Analysis and Visualisation<br>- CSC3063: Secure Software Development<br>- CSC3064: Network Security<br>- CSC3065: Cloud Computing<br>"
                         + "- CSC3066: Deep Learning<br>- CSC3067: Video Analytics and Machine Learning<br>- CSC3068: Software Development Practice<br>- CSC3069: Software Engineering Enterprise Project<br>")
        



    # def test_like_response(self):            ##### Manual Test
    #     message = "I like coding"
    #     response = str(chatbot.get_response(message))
    #     print(response)
    #     response_bool = response_type_func()
    #     self.assertTrue(response_bool)

    # Chatbot identifies the input as having a positive sentient towards coding
    
    # def test_dislike_response(self):         ##### Already tested
    #     message = "I dislike programming"
    #     response = str(chatbot.get_response(message))
    #     self.assertEqual(response, "Thanks for providing me with this information. I won't recommend any modules that contain programming.")


       # def test_null_response(self): ##### Manual Test
    #     message = ""
    #     response = str(chatbot.get_response(message))
    #     print(response)
    #     response_bool = response_type_func()
    #     self.assertTrue(response_bool)

    # def test_pathway_input(self): ######### Gives too many different answers
    #     message = "List modules for Computer Science pathway"
    #     response = str(chatbot.get_response(message))
    #     self.assertEqual(response, "I am sorry, but I do not understand.")
        # Should fail as functionality to show modules for a pathway is not implemented yet.

    # def test_for_chatbot_instructions(self):  ######### Gives too many different answers
    #     message = "Help"
    #     response = str(chatbot.get_response(message))
    #     self.assertEqual(response, "I am sorry, but I do not understand.")
        # Should fail as functionality to show instructions is not implemented yet.

                                            


# def response_type_func():
#         response_type = input("Enter 1 if this is a positive response,\nEnter 0 if this is a negative response: ")
#         response_bool = ""
#         if (response_type == ("1")):
#             response_bool = True
#         elif (response_type == ("0")):
#             response_bool = False
#         else:
#             print("Must enter either 1 or 0.")
#             response_type_func()
#         return response_bool


if __name__ == '__main__':
    unittest.main()
