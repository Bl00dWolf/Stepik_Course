class Testpaper:
    def __init__(self, obj: str, answers: list[str], min_score: str):
        self.obj = obj
        self.answers = answers
        self.min_score = min_score


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, test: Testpaper, stud_answers: list[str]):
        correct, max_cor = 0, len(test.answers)
        if isinstance(self.tests_taken, str):
            self.tests_taken = {}

        for stud, right in zip(stud_answers, test.answers):
            if stud == right:
                correct += 1

        proc_of_right = round(correct / max_cor * 100)
        self.tests_taken[
            test.obj] = f"{('Failed! ', 'Passed! ')[proc_of_right >= int(test.min_score[:-1])]}({proc_of_right}%)"
