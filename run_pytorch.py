import torch

import time

# add = torch.tensor([0]).cuda()

add = torch.tensor([0]).cuda()

while True:
    add = add + 1
    time.sleep(60)
    print( 'now run to iter: ', add )
    if add > 10000:
        break




