"""

path is the path to a directory of csv files

returns a pandas df

"""

import pandas as pd
import glob

def dl_panda_frame(path):

    # path = '../prepare/analysis' # use your path
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        print(filename)
        #df = pd.read_csv(filename, index_col=None, header=0)
        df = pd.read_csv(filename, index_col=None, header=None, dtype=str)
        li.append(df)
    

    PANDA_FRAME = pd.concat(li, axis=0, ignore_index=True)

    return(PANDA_FRAME)


def dl_select_path_row(df_in, path, row):
    pf = df_in
    nf = pf.loc[pf['Path']==path]
    AOI_PF = nf.loc[nf['Row']==row]
    return(AOI_PF)



def dl_generate_list_of_xmls(bucket, panda_frame):
    column_names = list(panda_frame.columns)
    print(column_names)
    paths=[]
    for index, row in panda_frame.iterrows():
        #print(row.values)
        full_path = '/'.join(row.values)
        #print(full_path)
        full_path = 's3://'+ bucket + '/' + full_path
        paths.append(full_path)
    return(paths)

