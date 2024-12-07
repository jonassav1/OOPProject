import pytest
from unittest.mock import patch, mock_open
from practice_mode import Practice

def test_get_asnwer():
    practice = Practice()
    question_data = { 
        "question" : "whats 2+2?",
        "answers" : ["1", "2", "3", "4"]
    }
    with patch("builtins.input" ,return_value = "4"):
        answer = practice.get_answer(question_data)
        assert answer == 4

def test_check_answers():
    practice = Practice()
    question_data = {
        "question" : "whats 2+2?",
        "answers" : ["1", "2", "3", "4"],
        "correct_answer" : "4"
        }
    assert practice.check_answer(question_data, 4) == True
    assert practice.check_answer(question_data, 1) == False

def test_get_question():
    practice = Practice()
    mock_file_data = "1,True,4,whats 2+2?,1,2,3,4,0,0,0,"
    with patch('builtins.open', mock_open(read_data=mock_file_data)):
        practice.get_questions()
        assert practice.quiz_questions[0]["question"] == "whats 2+2?"
        assert practice.quiz_questions[0]["answers"] == ["1", "2", "3", "4"]
        assert practice.quiz_questions[0]["correct_answer"] == "4"
