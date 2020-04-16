import pandas as pd


def bestseller():
    filename = "assign11-1-catering_sale_all.xls"
    data = pd.read_excel(filename, header=None)

    try:
        datesel = int(input("Please enter the day for which you would like the best seller (1-31): "))
        if datesel < 1 or datesel > 31:
            raise ValueError
        if (datesel > 8 and datesel < 12):
            print("No sales data for that date")
            exit()
        if datesel > 11:
            datesel = datesel - 3

        sales = data.loc[datesel].tolist()[1:]
        maxsale = max(sales)

        ind = [index for index, val in enumerate(sales) if val == maxsale]

        if len(ind) > 1:
            print("The best sellers for {:%Y-%m-%d} were: ".format(data[0][datesel]))
            for i in range(len(ind)):
                print(data[ind[i] + 1][0])
            print("Each sold {0} units".format(maxsale))

        else:
            print("The best seller for {:%Y-%m-%d}".format(data[0][datesel]), " was {0}, selling {1} units".format(data[ind[0] + 1][0], maxsale))
    except ValueError:
        print("That is not a valid date")


bestseller()

