import pandas as pd

def load_csv(file_name="first.csv"):
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        print("CSV file not found.")
        return None

def sort_data(df, column_name):
    try:
        sorted_df = df.sort_values(by=column_name, ascending=True)
        return sorted_df
    except Exception:
        print("Column not found for sorting.")
        return df

def search_data(df, column_name, value):
    try:
        result = df[df[column_name] == value]
        return result
    except Exception:
        print("Search column not found.")
        return pd.DataFrame()

def show_summary(df):
    return df.describe(include="all")

def export_data(df, file_name="output.csv"):
    df.to_csv(file_name, index=False)
    print(f"Data exported to {file_name}")

def main():
    data = load_csv()

    if data is None:
        return

    print("\n--- Summary of Data ---")
    print(show_summary(data))

    print("\n--- Sorted Data Example ---")
    column_to_sort = input("Enter column name to sort by: ")
    sorted_data = sort_data(data, column_to_sort)
    print(sorted_data.head())
    export_data(sorted_data, "sorted_output.csv")

    print("\n--- Search Function ---")
    search_col = input("Enter column to search: ")
    search_val = input("Enter value to find: ")
    results = search_data(data, search_col, search_val)
    if results.empty:
        print("No matching records found.")
    else:
        print(results)

if __name__ == "__main__":
    main()
