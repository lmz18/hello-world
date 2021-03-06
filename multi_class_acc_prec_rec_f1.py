def multi_class_accuracy_precision_f1score(y_true, y_pred, num_classes):
    # calculates accuracy, weighted precision, and weighted f1-score for n-class classification for n>=3
    # note that weighted recall is the same as accuracy

    N = len(y_true)
    confusion_matrix = [[0 for _ in range(num_classes)] for _ in range(num_classes)]

    for i in range(0, N):
        confusion_matrix[y_true[i]][y_pred[i]] += 1

    sum_diagonal = 0
    
    for i in range(0, num_classes):
        sum_diagonal += confusion_matrix[i][i]

    precision = 0.0
    f1score = 0.0

    for i in range(0, num_classes):
        support = 0
        sum_column = 0

        for j in range(0, num_classes):
            support += confusion_matrix[i][j]
            sum_column += confusion_matrix[j][i]

        if support != 0:
            g = confusion_matrix[i][i] * support
            f1score += g / (support + sum_column)

            if sum_column != 0:
                precision += g / sum_column

    accuracy = sum_diagonal / N
    precision /= N
    f1score = 2 * f1score / N

    return accuracy, precision, f1score
