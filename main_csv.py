import os
import pandas as pd

def main():
    dir=os.getcwd()
    directory = os.path.join("c:\\","path")
    for root,dirs,files in os.walk(dir):
        for file in files:
           if file.endswith(".csv"):
               try:
                   df = pd.read_csv(file)
               except:
                   df = pd.read_csv(file, sep="|")
               name=file.split(".")
               filename=name[0]+"_utf_8.csv"
               df.to_csv(filename,encoding='utf-8-sig')
               #f=open(file, 'r')
               #  perform calculation
               #f.close()

if __name__ == "__main__":
    main()