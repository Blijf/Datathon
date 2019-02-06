import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#..................................................................
#                      LECTURA csv
#..................................................................

df=pd.read_csv('Modelar_UH2019.txt', sep="|")

df.info()


