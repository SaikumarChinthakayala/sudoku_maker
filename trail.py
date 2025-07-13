import numpy as np
grid=np.zeros((9,9))
base=np.array([1,2,3,4,5,6,7,8,9])
# Define blocks as tuples of slice objects
block0 = (slice(0, 3), slice(0, 3))
block1 = (slice(0, 3), slice(3, 6))
block2 = (slice(0, 3), slice(6, 9))
block3 = (slice(3, 6), slice(0, 3))
block4 = (slice(3, 6), slice(3, 6))
block5 = (slice(3, 6), slice(6, 9))
block6 = (slice(6, 9), slice(0, 3))
block7 = (slice(6, 9), slice(3, 6))
block8 = (slice(6, 9), slice(6, 9))


grid[block0]=np.random.choice(base,size=(3,3),replace=False)
grid[block4]=np.random.choice(base,size=(3,3),replace=False)
grid[block8]=np.random.choice(base,size=(3,3),replace=False)

block_list = [block1, block2, block3, block5, block6, block7]

for block in block_list:
    block_row_start,block_column_start=block
    temp_base=np.array([1,2,3,4,5,6,7,8,9])
    print(block)
    for i in range(3):
        for j in range(3):
            mask = ~np.isin(temp_base,np.unique(np.concatenate((grid[block_row_start.start+i,:],grid[:,block_column_start.start+j]))))
            print(mask)
            fill_base=temp_base[mask]
            print(fill_base)
            grid[block_row_start.start+i,block_column_start.start+j]=fill_base[0]
            temp_base=temp_base[temp_base!=fill_base[0]]
            print("temp_base=",temp_base)
            print(grid)
    
            
