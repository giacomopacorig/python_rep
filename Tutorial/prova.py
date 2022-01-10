import numpy as np

data = np.array([[833. ,  37. ],
                 [987. ,  41.6],
                 [883. ,  37.2],
                 [378. ,  15.2],
                 [ 84. ,   3.4],
                 [483. ,  19.6],
                 [835. ,  35.1],
                 [646. ,  28.9],
                 [508. ,  22.6],
                 [ 90. ,   3.7]])

km_tragitto = [2500. , None];
data.update(km_tragitto);

print(data);