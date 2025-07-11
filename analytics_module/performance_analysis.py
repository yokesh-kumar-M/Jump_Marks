def identify_weak_subjects(df):
    return df[df['Grade Point'] < 7]

def improvement_suggestions(df, target_cgpa):
    df = df.copy()
    suggestions = []
    for i, row in df.iterrows():
        original_gp = row['Grade Point']
        for new_gp in range(original_gp + 1, 11):
            df.at[i, 'Grade Point'] = new_gp
            new_cgpa = (df['Grade Point'] * df['Credit']).sum() / df['Credit'].sum()
            if new_cgpa >= target_cgpa:
                suggestions.append({
                    'Subject': row['Subject'],
                    'Required GP': new_gp,
                    'Required Marks': (new_gp - 1) * 10
                })
                break
        df.at[i, 'Grade Point'] = original_gp
    return suggestions
