#from index_lib import index_records

def cli():
    print ("Hello Tony")

    for path in range (40,41):
        for row in range (30,33):
            for year in range(2013,2019+1):
                print(path, row, year)


if __name__ == '__main__':
    cli()
