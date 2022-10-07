class Model:

    # constructor:
    def __init__(self, mean_map, int_map, df_sampled):
        self.mean_map = mean_map
        self.int_map = int_map
        self.df_sampled = df_sampled
    
    # display:
    def display(self):
        print('numerical conversions:')
        print(self.int_map)
        print('---')
        print('mean map:')
        print(self.mean_map)
        print('---')
        print('sampled cached data:')
        print(self.df_sampled)