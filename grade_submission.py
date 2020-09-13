TOLERANCE = 1e-6

from string import printable

def parseFile(inFile):
    lines = inFile.readlines()
    for i in range(len(lines)):
        # Remove pesky non-printable characters
        stripped = ''.join([char for char in lines[i] if char in printable]) 
        lines[i] = stripped.split(",") 
        if len(lines[i]) != 3:
            raise Exception("Parse Error on line {}: line must contain exactly 3 comma separated values.".format(i+1)) 
        try:
            lines[i] = (int(lines[i][0]), float(lines[i][1]), float(lines[i][2]))
        except ValueError as e: 
            raise Exception("Parse Error on line {}. {}".format(i + 1, str(e)))

    return lines

def gradeFile(submission, ground_truth, truncation_value=None, truncation_message=True):
    # Assuming the ground-truth file is perfectly formatted 
    ground = parseFile(ground_truth)

    if truncation_value is None or truncation_value > len(ground):
        truncation_value = len(ground)

    try:
        sub = parseFile(submission)
        message = ""
        score = 0

        for i in range(len(sub)):
            if i >= truncation_value: 
                score = truncation_value 
                if truncation_message:
                    message += "Score truncated to {}.\n".format(len(ground))
                break
            elif abs(ground[i][1] - sub[i][1]) > TOLERANCE:
                message += "Incorrect value on line {}.\n".format(i+1)
                break
            else:
                score += 1

        message += "First {} values were computed correctly in current submission.".format(score)
        return score, message

    except Exception as e:
        return 0, str(e) 



if __name__ == '__main__':
    '''
    Calling this script directly grades the provided submission.csv file against the provided ground_truth.csv file.
    The ground truth file provided to you only has the first 5 values, so if all works correctly, you should see
    "First 5 values computed correctly in current submission" (and otherwise an error message)
    '''
    print("")
    print(gradeFile(open("submission.csv"), open("ground_truth.csv"), truncation_value=5, truncation_message=False)[1])