# ResearchFrame Class
import pandas as pd
import re


def condense_title(title):
    acronyms = re.findall(r'\b[A-Z]{2,}\b', title)
    if acronyms:
        condensed_title = ' '.join(acronyms)  # Join acronyms with spaces
    else:
        condensed_title = title  # Use the full title if no acronyms are found
    return condensed_title


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
    def __init__(self, input, output, templates, sheet):
        self.sheet = sheet
        self.input_df = pd.read_excel(input, sheet_name=self.sheet)
        self.output = output
        self.templates = templates
        self.df = self.input_df[['LeadROName', 'PISurname', 'PIFirstName', 'Title']].copy()

        # Generate email addresses
        self.df.loc[:, 'Email'] = self.df.apply(
            lambda row: generate_email(row['PIFirstName'], row['PISurname'], row['LeadROName'], self.templates),
            axis=1)

        # Condense the project title using the condense_title function
        self.df.loc[:, 'CondensedTitle'] = self.df['Title'].apply(condense_title)

        # Select the relevant columns
        self.df = self.df[['LeadROName', 'PISurname', 'PIFirstName', 'Email', 'CondensedTitle']]

    def output_xl(self):

        self.df.to_excel(self.output, index=False)
        print("Processing complete. Output saved to", self.output)



