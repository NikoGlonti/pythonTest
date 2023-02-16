import random
import string

import matplotlib.pyplot as plt
import os
import pandas as pd
import warnings
import matplotlib

warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)

url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"


class DrawingPlots:
    def __int__(self, url=None):
        self.url = url

    def draw_plots(self):
        df = pd.read_json(self.url)
        df.to_json('example.json')
        '''df_f = pd.read_json('example.json')'''
        df.plot(x="min", y=["max", "name"], kind="bar", figsize=(9, 8))
        script_dir = os.path.dirname(__file__)
        results_dir = os.path.join(script_dir, 'plots/')
        file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        if not os.path.isdir(results_dir):
            os.makedirs(results_dir)
        plt.savefig(results_dir + file_name)
        return os.path.join(script_dir, results_dir)
