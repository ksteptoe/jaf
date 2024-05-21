# ResearchFrame Class
import pandas as pd


# Function to generate email addresses
def generate_email(first_name, last_name, institution, templates):
    template = templates.get(institution)
    if not template:
        return None
    first_initial = first_name[0].lower()
    last_initial = last_name[0].lower()
    email = template.format(first=first_name.lower(), last=last_name.lower(), f=first_initial, l=last_initial)
    return email


class ResearchFrame:
    def __init__(self, templates, file):
        input_df = pd.read_excel(file, sheet_name='Table1')
        self.templates = templates
        self.df = input_df

        df = self.df[['LeadROName', 'PISurname', 'PIFirstName', 'Title']].copy()

        # Generate email addresses
        df.loc[:, 'Email'] = df.apply(
            lambda row: generate_email(row['PIFirstName'], row['PISurname'], row['LeadROName'], self.templates),
            axis=1)

        # Condense the project title if necessary (for example, by trimming)
        df['CondensedTitle'] = df['Title'].str.strip()

    def guess_email(self, row):
        return self.email_pattern[row['LeadROName']]


