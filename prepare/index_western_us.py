from index_lib import index_records
import timeit

def cli():
    print ("Hello Tony")

    start = timeit.timeit()
    for path in range (31,46):
        for row in range (26,38):
            for year in range(2013,2019+1):
                print(path, row, year)
                index_records(path,row,year)
    end = timeit.timeit()
    print("TIMED = ", end - start)


if __name__ == '__main__':
    cli()


