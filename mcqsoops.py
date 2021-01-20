
class mcqs:

    qns = []
    answers = []

    def __init__(self, file_path, answers_path):
        self.path = file_path
        self.answers_path = answers_path

    def makeStatements(self):
        ''' converts text file to sentences '''
        import re
        with open(self.path, 'r+') as f:
            data = f.read()
            sentences = re.split(r' *[\.\?!][\'"\)\]]* *', data)
            return sentences

    def createAnswers(self):
        ''' returns correct answers '''
        import csv
        with open(self.answers_path, 'r+') as f:
            text = csv.reader(f, delimiter = ',')
            for l in text:
                self.answers.append(l)
            answers = self.answers[0]
        return answers
                

    def makeMCQs(self, sentences, answers):
        ''' creates MCQs from sentences and answers '''
        for (row, word) in zip(sentences, answers):
            if word in row:
                self.qns.append(row.replace(word, '[               ]'))
        return self.qns

    def saveQns(self, savefilepath, qns, answers):
        ''' saves MCQs in required location '''
        import csv
        with open(savefilepath, 'w') as f:
            mcqs = csv.writer(f)
            for (row, word) in zip(self.qns, answers):
                mcqs.writerow([row, word])


##if __name__ == '__main__':
##    data = mcqs('D:\\Work\\Python\\Scripts\\mcqs\\sample-text.txt', 'D:\\Work\\Python\\Scripts\\mcqs\\answers.txt')
##    statements = data.makeText()
##    answers = data.correctAnswers()
##    print(statements)
##    print(answers)
##    qns = data.makeMCQs(statements, answers)
##    data.saveQns('D:\\Work\\Python\\Scripts\\mcqs\\qns.csv', qns, answers)
