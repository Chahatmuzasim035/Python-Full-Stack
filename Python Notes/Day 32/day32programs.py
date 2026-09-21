# Day 32 - Pandas Programs
# Install Pandas if required:
# pip install pandas

import pandas as pd


# Common product dataset used in the examples
data = {
    "Product": ["Wireless Earbuds", "Smartphone", "Laptop",
                "Smartwatch", "Bluetooth Speaker"],
    "Brand": ["SoundMax", "TechNova", "ByteCore",
              "TimeTrack", "EchoBoom"],
    "Price": [2999, 15999, 52999, 4999, 1999],
    "Stock": [50, 30, 20, 40, 60]
}

df = pd.DataFrame(data)


# 1. Create a Series
def program_1():
    prices = pd.Series(
        [2999, 15999, 52999, 4999, 1999],
        index=["Earbuds", "Smartphone", "Laptop",
               "Smartwatch", "Speaker"]
    )

    print(prices)


# 2. Create a DataFrame
def program_2():
    print(df)


# 3. Series methods
def program_3():
    prices = pd.Series([2999, 15999, 52999, 4999, 1999])

    print("Mean:", prices.mean())
    print("Sum:", prices.sum())
    print("Maximum:", prices.max())
    print("Minimum:", prices.min())
    print("First values:")
    print(prices.head(3))
    print("Sorted:")
    print(prices.sort_values())


# 4. DataFrame attributes and information
def program_4():
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("Index:", df.index)
    print("\nInfo:")
    df.info()
    print("\nDescription:")
    print(df.describe())


# 5. Select columns
def program_5():
    print("Product column:")
    print(df["Product"])

    print("\nProduct and Price:")
    print(df[["Product", "Price"]])


# 6. Filter rows
def program_6():
    expensive = df[df["Price"] > 10000]
    print(expensive)


# 7. loc and iloc
def program_7():
    print("Using loc:")
    print(df.loc[1, "Product"])

    print("Using iloc:")
    print(df.iloc[1, 2])


# 8. Missing values
def program_8():
    data_with_missing = {
        "Product": ["A", "B", "C", "D"],
        "Price": [100, None, 300, None]
    }

    sample = pd.DataFrame(data_with_missing)

    print("Original:")
    print(sample)

    print("\nMissing count:")
    print(sample.isnull().sum())

    print("\nDrop missing:")
    print(sample.dropna())

    print("\nFill missing with 0:")
    print(sample.fillna(0))

    print("\nInterpolate:")
    print(sample.interpolate())


# 9. Change data type
def program_9():
    sample = pd.DataFrame({"Price": [100, 200, 300]})

    sample["Price"] = sample["Price"].astype(float)
    print(sample)
    print(sample.dtypes)


# 10. Rename and drop columns
def program_10():
    sample = df.copy()

    sample.rename(columns={"Product": "Product Name"}, inplace=True)
    sample.drop(columns=["Stock"], inplace=True)

    print(sample)


# 11. GroupBy and aggregation
def program_11():
    print("Average price by brand:")
    print(df.groupby("Brand")["Price"].mean())

    print("\nMultiple aggregations:")
    print(df.groupby("Brand").agg({
        "Price": ["mean", "max", "min"]
    }))


# 12. Sorting and ranking
def program_12():
    sorted_df = df.sort_values(by="Price", ascending=False)
    print("Sorted:")
    print(sorted_df)

    ranked = df.copy()
    ranked["Rank"] = ranked["Price"].rank(ascending=False)
    print("\nRanked:")
    print(ranked)


# 13. Concatenate DataFrames
def program_13():
    df1 = pd.DataFrame({
        "Product": ["A", "B"],
        "Price": [100, 200]
    })

    df2 = pd.DataFrame({
        "Product": ["C", "D"],
        "Price": [300, 400]
    })

    print("Row-wise:")
    print(pd.concat([df1, df2], axis=0, ignore_index=True))

    print("\nColumn-wise:")
    print(pd.concat([df1, df2], axis=1))


# 14. Merge DataFrames
def program_14():
    df1 = pd.DataFrame({
        "Product": ["A", "B", "C"],
        "Price": [100, 200, 300]
    })

    df2 = pd.DataFrame({
        "Product": ["A", "B", "D"],
        "Stock": [10, 20, 30]
    })

    merged = pd.merge(df1, df2, on="Product", how="inner")
    print(merged)


# 15. Pivot table
def program_15():
    sample = pd.DataFrame({
        "Brand": ["A", "A", "B", "B"],
        "Stock": [10, 20, 10, 20],
        "Price": [100, 150, 200, 250]
    })

    pivot = sample.pivot_table(
        values="Price",
        index="Brand",
        columns="Stock",
        aggfunc="mean"
    )

    print(pivot)


# 16. Cross tabulation
def program_16():
    sample = pd.DataFrame({
        "Brand": ["A", "A", "B", "B", "A"],
        "Stock": [10, 20, 10, 20, 10]
    })

    print(pd.crosstab(sample["Brand"], sample["Stock"]))


# 17. Time series operations
def program_17():
    sample = pd.DataFrame({
        "Purchase Date": ["2026-01-05", "2026-01-15",
                          "2026-02-05", "2026-02-20"],
        "Sales": [1000, 1500, 1200, 1800]
    })

    sample["Purchase Date"] = pd.to_datetime(sample["Purchase Date"])
    sample.set_index("Purchase Date", inplace=True)

    print(sample)
    print("\nMonthly data:")
    print(sample.resample("ME").mean())


# 18. Pandas visualization
def program_18():
    # Uncomment plt.show() if running in an environment
    # where graphical plots are supported.
    ax = df.plot(
        x="Product",
        y="Price",
        kind="bar",
        title="Product Prices"
    )

    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig("product_prices.png")
    print("Bar chart saved as product_prices.png")


# 19. Apply and map
def program_19():
    prices = pd.Series([1000, 2000, 3000])

    print("Apply:")
    print(prices.apply(lambda x: x * 2))

    print("\nMap:")
    print(prices.map(lambda x: x + 500))


# 20. Value counts
def program_20():
    brands = pd.Series(["A", "B", "A", "C", "B", "A"])

    print(brands.value_counts())


if __name__ == "__main__":
    program_1()
    program_2()
    program_3()
    program_4()
    program_5()
    program_6()
    program_7()
    program_8()
    program_9()
    program_10()
    program_11()
    program_12()
    program_13()
    program_14()
    program_15()
    program_16()
    program_17()
    program_18()
    program_19()
    program_20()
