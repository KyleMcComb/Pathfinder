import re
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

class InterestAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        statement_text = statement.text.lower()
        return re.search(r'\b(like|dislike|hate)\b', statement_text) is not None

    def process(self, input_statement, additional_response_selection_parameters=None): 
        statement_text = input_statement.text.lower()
        response = Statement('')

        dislike_match = re.search(r'\bdislike\b', statement_text)
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

        interest_match = re.search(r'\b(?:ai|network security)\b', interest)
        if interest_match:
            interest = interest_match.group()

        if response_type == 'like':
            if 'ai' == interest:
                response.text = f"That's great! I would recommend this AI module: CSCAI (placeholder)"
            elif 'network security' == interest:
                response.text = f"That's great! I would recommend this network security module: CSC3064 Network Security"
            else:
                response.text = f"You like {interest}. I will try and recommend any modules that contains {interest}."
                # Add more custom responses for other interests here
        else:
            if 'ai' == interest:
                response.text = f"Thanks for providing me with this information. I won't recommend any modules that contain AI."
            elif 'network security' == interest:
                response.text = f"Thanks for providing me with this information. I won't recommend any modules that contain Network Security."
            else:
                response.text = f"You dislike {interest}. I will try and not recommend any modules that contains {interest}."
                # Add more custom responses for other interests here

        response.confidence = 1
        return response