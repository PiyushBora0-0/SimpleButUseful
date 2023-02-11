def split_para(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        paragraphs = text.split(',')
        result = []
        paragraph = ''
        for para in paragraphs:
            if len(paragraph + para) > 1000:
                result.append(paragraph)
                paragraph = ''
            paragraph += para + ', '
        result.append(paragraph)

    return result

def insert_newline(file_path):
    paragraphs = split_para(file_path)
    with open(file_path, 'w') as file:
        for para in paragraphs:
            file.write(para + '\n\n\n\n')

# Call the function with the file path
insert_newline('input.txt')
