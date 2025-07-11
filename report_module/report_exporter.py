def export_to_excel(df, filename='cgpa_report.xlsx'):
    df.to_excel(filename, index=False)
    print(f"Exported to {filename}")
