from survery import ANonymousSurvey

# Define a question, and make a survey.
question = "What language  did you first learn to speak?"
language_survey = ANonymousSurvey(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n" )
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_presponse(response)

# Show the survey results.
print("\nblablalbalbalbalblalbal")
language_survey.show_results()