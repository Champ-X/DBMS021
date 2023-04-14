def process_courses_data():
    courses_data_path = 'courses_zh_en.txt'
    courses_zh_data_path = 'courses_zh.txt'
    current_courses = []  # 为了去重
    with open(courses_data_path, 'r') as inputFile:
        line = inputFile.readline().strip().split()
        outputFile = open(courses_zh_data_path, 'w')
        while line:
            if line[0] not in current_courses:
                current_courses.append(line[0])
                outputFile.write(line[0] + '\n')
            line = inputFile.readline().strip().split()
        inputFile.close()
        outputFile.close()


if __name__ == '__main__':
    process_courses_data()
