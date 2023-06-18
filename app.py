import streamlit as st
import requests

# API_URL = 'http://127.0.0.1:8000/get-question-api/'
API_URL ="http://aittages.pythonanywhere.com//get-question-api"

def get_questions(text):

    payload = {'text': text}
    response = requests.get(API_URL, params=payload)

    response_dct = response.json()

    return response_dct["text_with_spans"], response_dct["question"],response_dct["answers"] ,int(response_dct["correct_answer_index"])

text = st.text_area(label="Enter the text for question generation")

click = st.button("Generate some questions!")

if st.session_state.get('button') != True:

    st.session_state['button'] = click
    # st.write(f"Generate button is {click}")

if st.session_state['button'] == True:

    text_with_spans, question, answers, correct_answer_index = get_questions(text)
    correct_answer = answers[correct_answer_index]

    st.write("***The generated question is below:***\n")
    st.write(question)

    click_dict = {}

    for ans in answers:
        click_dict[ans] = st.button(ans)

    if any([click_dict[ans] for ans in click_dict.keys()]):

        for ans in click_dict.keys():
            if click_dict[ans]:
                selected_answer = ans
                break
        if selected_answer == correct_answer:
            st.write("Correct!")
        else:
            st.write(f"Incorrect! The right answer is {correct_answer}")

        st.write("***Text with span related to the answer is below***")
        st.write(text_with_spans)

        st.session_state['button'] = False

        st.button('Reload')