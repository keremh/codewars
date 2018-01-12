"""
The first input array contains the correct answers to an exam, like ["a", "a", "b", "d"]. The second one is "answers" array and contains student's answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty string).

If the score < 0, return 0.
"""

def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score = score + 4
        elif arr1[i] == "" or arr2[i] == "":
            continue
        else:
            score = score - 1
    if score < 0:
        score = 0
    return score


