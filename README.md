This directory includes a few sample datasets to get you started.

*   `california_housing_data*.csv` is California housing data from the 1990 US
    Census; more information is available at:
    https://developers.google.com/machine-learning/crash-course/california-housing-data-description

*   `mnist_*.csv` is a small sample of the
    [MNIST database](https://en.wikipedia.org/wiki/MNIST_database), which is
    described at: http://yann.lecun.com/exdb/mnist/

*   `anscombe.json` contains a copy of
    [Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet); it
    was originally described in

    Anscombe, F. J. (1973). 'Graphs in Statistical Analysis'. American
    Statistician. 27 (1): 17-21. JSTOR 2682899.

    and our copy was prepared by the
    [vega_datasets library](https://github.com/altair-viz/vega_datasets/blob/4f67bdaad10f45e3549984e17e1b3088c731503d/vega_datasets/_data/anscombe.json).

This directory includes a few sample datasets to get you started.

california_housing_data*.csv is California housing data from the 1990 US Census; more information is available at: https://developers.google.com/machine-learning/crash-course/california-housing-data-description

mnist_*.csv is a small sample of the MNIST database, which is described at: http://yann.lecun.com/exdb/mnist/

anscombe.json contains a copy of Anscombe's quartet; it was originally described in

Anscombe, F. J. (1973). 'Graphs in Statistical Analysis'. American Statistician. 27 (1): 17-21. JSTOR 2682899.

and our copy was prepared by the vega_datasets library.

Висновки:
1. Сортування злиттям показало стабільну продуктивність на всіх розмірах масивів, що підтверджує його часову складність O(n log n).
2. Сортування вставками виявилося дуже повільним на великих наборах даних, що підтверджує його часову складність O(n^2). На малих наборах даних воно може бути ефективним.
3. Timsort (вбудована функція sorted) показала найкращі результати на всіх розмірах масивів, завдяки поєднанню сортування злиттям та сортування вставками. Це підтверджує ефективність алгоритму Timsort.
4. Вбудовані алгоритми сортування в Python (Timsort) є найефективнішими і їх варто використовувати у більшості випадків замість реалізації власних алгоритмів сортування.