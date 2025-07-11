def grade_point(marks):
    if marks >= 90: return 10
    elif marks >= 80: return 9
    elif marks >= 70: return 8
    elif marks >= 60: return 7
    elif marks >= 50: return 6
    else: return 5

def calculate_cgpa(df):
    df['Grade Point'] = df['Marks'].apply(grade_point)
    total_credits = df['Credit'].sum()
    weighted_sum = (df['Credit'] * df['Grade Point']).sum()
    cgpa = round(weighted_sum / total_credits, 2)
    return cgpa
