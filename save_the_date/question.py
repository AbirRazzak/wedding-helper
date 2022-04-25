from enum import Enum


class SaveTheDateQuestions(str, Enum):
    full_name = 'What is your full name?'
    email_address = 'What is your email address?'
    plus_ones = 'Who else is coming with you? (Indicate age if under 13, full names please)'
    hotel_needed = 'Do you need us to help book a hotel room?'
    vaccinated = 'Are you vaccinated against COVID-19?'
