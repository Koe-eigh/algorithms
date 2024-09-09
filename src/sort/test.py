import time
import random

import algorithms

# テストデータの生成
def generate_test_data():
    # 1. ランダムな数値リスト
    random_list = [random.randint(0, 1000) for _ in range(10)]

    # 2. 昇順に整列されたリスト
    sorted_list = [i for i in range(10)]

    # 3. 降順に整列されたリスト
    reverse_sorted_list = [i for i in range(10, 0, -1)]

    # 4. 全て同じ値のリスト
    same_value_list = [5 for _ in range(10)]

    # 5. 既にソートされているが、一部に異常値が混じっているリスト
    almost_sorted_list = [1, 2, 3, 4, 1000, 5, 6, 7, 8, 9]

    return {
        "random_list": random_list,
        "sorted_list": sorted_list,
        "reverse_sorted_list": reverse_sorted_list,
        "same_value_list": same_value_list,
        "almost_sorted_list": almost_sorted_list
    }

# テストデータの生成
test_data = generate_test_data()

def test(algorithm):
    print(f'{algorithm}')
    for list_name, test_list in test_data.items():
        start_time = time.time()
        algorithm(test_list)
        end_time = time.time()
        print(f'{list_name} {test_list} 実行時間: {end_time - start_time}秒')
# test(algorithms.bogo_sort)
test(algorithms.bubble_sort)
test(algorithms.cocktail_sort)
test(algorithms.comb_sort)
test(algorithms.selection_sort)
test(algorithms.gnome_sort)
test(algorithms.insertion_sort)
test(algorithms.quick_sort)
