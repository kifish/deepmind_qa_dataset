import os, glob
from tqdm import tqdm

def create_data(path_to_corpus, output_name):
    '''
        path_to_corpus : the directory to CNN/Daily Mail where stores, questions folder are located
    '''
    output_f = open(output_name, 'w')
    for question_filename in tqdm(glob.glob(os.path.join(path_to_corpus, '*.question'))):
        with open(question_filename, 'r') as q:
            content = q.readlines()[2:] # skip urls and newline at the beginning
            document = content[0]
            question = content[2]
            answer = content[4]

            output_f.write(question)
            output_f.write(answer)
            output_f.write(document)
            output_f.write('\n')

    output_f.close()

if __name__ == '__main__':
    path_to_corpus = './cnn/questions/training/'
    output_file_path = './cnn/questions/cnn_train.txt'
    create_data(path_to_corpus, output_file_path)

    path_to_corpus = './cnn/questions/validation/'
    output_file_path = './cnn/questions/cnn_dev.txt'
    create_data(path_to_corpus, output_file_path)

    path_to_corpus = './cnn/questions/test/'
    output_file_path = './cnn/questions/cnn_test.txt'
    create_data(path_to_corpus, output_file_path)
    