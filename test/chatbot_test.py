import unittest
from main.chatbot_settings import *
from main.chatbot import *
# Create your tests here.

#python Pathfinder/manage.py test Pathfinder.test.chatbot_test

class ChatbotTestCase(unittest.TestCase):

    def test_like_interest_with_web_scraped_data(self):
        message = "I like programming"
        response = str(chatbot.get_response(message))
        self.assertIn("modules related to programming", response)
        response = str(chatbot.get_response("2"))
        self.assertIn("relevant job roles", response)
        # Check if the response includes both module recommendations and career suggestions based on web-scraped data.

    def test_dislike_interest_with_web_scraped_data(self):
        message = "I dislike history"
        response = str(chatbot.get_response(message))
        self.assertIn("won't recommend any modules that contain history", response)
        # Check if the chatbot correctly responds to dislikes without including irrelevant module or career recommendations.

    def test_hate_interest_with_web_scraped_data(self):
        message = "I hate mathematics"
        response = str(chatbot.get_response(message))
        self.assertIn("won't recommend any modules that contain mathematics", response)
        # Ensure the chatbot correctly responds to hates without suggesting related modules or careers.

    def test_interest_with_no_matching_modules(self):
        message = "I like ancient languages"
        response = str(chatbot.get_response(message))
        self.assertIn("No specific modules found for ancient languages", response)
        self.assertIn("relevant job roles", response)
        # Verify the chatbot's response when there are no matching modules but there are career suggestions based on the interest.

    def test_interest_with_invalid_input(self):
        message = "I like 123456"
        response = str(chatbot.get_response(message))
        self.assertIn("Sorry, I do not understand", response)
        # Check the chatbot's response to nonsensical or irrelevant input.

    def test_interest_selection_process(self):
        message = "I like databases"
        response = str(chatbot.get_response(message))
        self.assertIn("modules related to databases", response)
        response = str(chatbot.get_response("1")) # Assuming there are at least 2 modules
        self.assertIn("updated your interest", response)
        # Test the process where a user selects a specific module based on their interests.

    def test_interest_selection_invalid_number(self):
        message = "I like databases"
        response = str(chatbot.get_response(message))
        self.assertIn("modules related to databases", response)
        response = str(chatbot.get_response("invalid_number"))
        self.assertIn("enter a number", response)
        # Check how the chatbot handles invalid module selection input.

    def test_interest_selection_out_of_range(self):
        message = "I like databases"
        response = str(chatbot.get_response(message))
        self.assertIn("modules related to databases", response)
        response = str(chatbot.get_response("999")) # Assuming an out-of-range number
        self.assertIn("enter a number between", response)
        # Ensure the chatbot correctly handles module selection numbers that are out of range.
        

    ### LanguageAdapter Test Cases ###

    def test_english_greeting(self):
        message = "hello"
        response = str(chatbot.get_response(message))
        self.assertEqual(response, "Hi")
        # Expecting an empty response as English is handled by other adapters.

    def test_german_greeting(self):
        message = "hallo"
        response = str(chatbot.get_response(message))
        self.assertIn("dieser Chatbot unterstützt nur Englisch", response)
        # Expecting a response in German indicating the chatbot supports only English.

    def test_spanish_greeting(self):
        message = "hola"
        response = str(chatbot.get_response(message))
        self.assertIn("este chatbot solo admite inglés", response)
        # Expecting a response in Spanish indicating the chatbot supports only English.

    def test_french_greeting(self):
        message = "bonjour"
        response = str(chatbot.get_response(message))
        self.assertIn("ce chatbot ne prend en charge que l'anglais", response)
        # Expecting a response in French indicating the chatbot supports only English.

    def test_chinese_greeting(self):
        message = "你好"
        response = str(chatbot.get_response(message))
        self.assertIn("此聊天机器人仅支持英语", response)
        # Expecting a response in Chinese indicating the chatbot supports only English.

    def test_numeric_input(self):
        message = "123"
        response = str(chatbot.get_response(message))
        self.assertIn("I do not understand", response)
        # Expecting a response indicating misunderstanding due to numeric input.

    def test_unrecognized_language(self):
        message = "Witam"
        response = str(chatbot.get_response(message))
        self.assertIn("Sorry, this chatbot only supports English", response)
        # Expecting a default response for unrecognized language.

    def test_empty_input(self):
        message = ""
        response = str(chatbot.get_response(message))
        self.assertIn("I do not understand", response)
        # Expecting a response indicating misunderstanding due to empty input.


    ### YearAdapter Test Cases ###
        
    def test_first_year_query(self):
        message = "I am a first year student"
        response = str(chatbot.get_response(message))
        self.assertIn("first-year modules you can do for EEECS", response)
        # Expecting a response listing first year modules.

    def test_second_year_query(self):
        message = "What are the modules for second year?"
        response = str(chatbot.get_response(message))
        self.assertIn("second-year modules you can do for EEECS", response)
        # Expecting a response listing second year modules.

    def test_final_year_query(self):
        message = "List final year modules"
        response = str(chatbot.get_response(message))
        self.assertIn("final year modules you can do for EEECS", response)
        # Expecting a response listing final year modules.

    def test_fourth_year_query(self):
        message = "Can you tell me about fourth year subjects?"
        response = str(chatbot.get_response(message))
        self.assertIn("fourth-year modules you can do for EEECS", response)
        # Expecting a response listing fourth year modules.

    def test_alternative_first_year_term(self):
        message = "What's in store for a year 1 student?"
        response = str(chatbot.get_response(message))
        self.assertIn("first-year modules you can do for EEECS", response)
        # Checking alternative phrasing for first year.

    def test_invalid_year_query(self):
        message = "I am in fifth year"
        response = str(chatbot.get_response(message))
        self.assertNotIn("modules you can do for EEECS", response)
        # Expecting the adapter not to respond to an unrecognized year.

    def test_numeric_input(self):
        message = "123"
        response = str(chatbot.get_response(message))
        self.assertNotIn("modules you can do for EEECS", response)
        # Expecting the adapter not to respond to numeric input unrelated to years.

    def test_unrelated_query(self):
        message = "How's the weather today?"
        response = str(chatbot.get_response(message))
        self.assertNotIn("modules you can do for EEECS", response)
        # The adapter should not respond to unrelated queries.


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
