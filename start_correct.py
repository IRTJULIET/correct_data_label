import pandas
from argparse import ArgumentParser

from correct_data_labels import CorrectLabels

def start_correct(num_of_wrongs, 
                    repeats, 
                    split_rate,
                    path,
                    epochs):
    if not num_of_wrongs:
        num_of_wrongs = [100]
    else:
        num_of_wrongs = [int(v) for v in num_of_wrongs]
    if not repeats:
        repeats = [1000]
    else:
        repeats = [int(v) for v in repeats]
    if not split_rate:
        split_rate = [50]
    else:
        split_rate = [int(v) for v in split_rate]
    if not path:
        path = '/home/dreamventures/hs/projects/CorrectDataLabel/data/train.csv'
        # path = '/Users/muratyalcin/Downloads/train.csv'
    def load_mnist_dataset(path):
        t = pandas.read_csv(path)
        cols = list(t.columns)
        cols = cols[1:] + [cols[0]]
        dataset = t[cols]
        return dataset
    num_of_wrongs = num_of_wrongs
    repeats = repeats
    split_rate = split_rate
    results = []
    print('loading dataset...')
    dataset = load_mnist_dataset(path)
    print('experiment started...')
    for i in num_of_wrongs:
        for j in repeats:
            for k in split_rate:
                cl = CorrectLabels(dataset = dataset,
                                    label_column_name = 'label', 
                                    epochs = epochs,
                                    num_of_wrongs = i, 
                                    repeats = j, 
                                    split_rate = k,
                                   mnist = True)
                print('\ncombination : \n', (i, j, k) , '\n')
                # result = cl.correct_wrong_labels_cnn()
                result = cl.correct_wrong_labels()
                results.append(result)
    res = pandas.DataFrame(results)
    res.to_csv('ml_results_2.csv')

if __name__=='__main__':
    parser = ArgumentParser()
    parser.add_argument('--num_of_wrongs', required = False,
    default = None, nargs = '+')
    parser.add_argument('--repeats', required = False, 
    default = None,  nargs = '+')
    parser.add_argument('--split_rate',  required = False, 
    default = None, nargs = '+')
    parser.add_argument('--path', type = str, required = False)
    parser.add_argument('--epochs', type = int, required = False, default = 10)
    args = parser.parse_args()

    start_correct(args.num_of_wrongs, 
                    args.repeats, 
                    args.split_rate,
                    args.path,
                    args.epochs)
