from hashlib import sha256

# Blockchain Class

class NinjaBlock:

    def __init__(self,data_list, previous_block_hash):
        
        self.data_list = data_list
        self.previous_block_hash = previous_block_hash

        self.block_data = '|' + "-".join(data_list) + "-" + previous_block_hash + '|'     # '|' and '-' are identifiers of the block,not necessary use any or not.
        self.block_hash = sha256(self.block_data.encode()).hexdigest()

data1 = 'BlockChain created'
data2 = "Feeding Data"
data3 = 'First Block Complete'

# You can add any amount of data in 1 block it's upto you

first_block = NinjaBlock([data1,data2,data3],'programmingninjas')   #Let programmingninjas be initial string,You can leave it empty.

data4 = 'Creating Second Block'
data5 = 'Feeding Data'
data6 = 'Second Block Complete'

second_block = NinjaBlock([data4,data5,data6],first_block.block_hash)
