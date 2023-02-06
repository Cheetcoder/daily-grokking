"""
5 Step Approach to leave your interviewer starstruck
The biggest mistake we see candidates make is not approaching the problem properly.

If I see you perform the following steps well, I will advocate to hire you. And most interviewers will too.

1. Write Examples and Clarify the Question: You need to write examples, and in the process, 
ask questions that unearth the actual problem the interviewer wants you to solve.
2. Come up with Solutions Come up with solutions and explain them to the interviewer, and once the interviewer
seems to settle on one, write down simple steps, not more than a few lines.
Doing this makes it clear (to both of you) what you will code for the rest of the interview.
3. Write down Test cases When an interviewer sees you do this, they know you are legit. Quickly jot down key test cases.
4. Write Code Write the actual code. Make liberal use of helper functions.
5. Verify code and test cases Once you are done, make sure you step through the code and make sure it works.

If you find it easier, use the acronym E.S.T.C.V (Examples, Solutions, Test Cases, Code, Verify).
"""


class MedianOfAStream:
    def insert_num(self, num):
        # TODO: Write your code here
        return

    def find_median(self):
        # TODO: Write your code here
        return 0


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
