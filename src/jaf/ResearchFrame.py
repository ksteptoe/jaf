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
    def __init__(self, templates, file):
        input_df = pd.read_excel(file, sheet_name='Table1')
        self.templates = templates
        self.df = input_df

        df = self.df[['LeadROName', 'PISurname', 'PIFirstName', 'Title']].copy()

        # Generate email addresses
        df.loc[:, 'Email'] = df.apply(
            lambda row: generate_email(row['PIFirstName'], row['PISurname'], row['LeadROName'], self.templates),
            axis=1)

        # Condense the project title using the condense_title function
        df.loc[:, 'CondensedTitle'] = df['Title'].apply(condense_title)
        # Select the relevant columns for the output
        output_df = df[['LeadROName', 'PISurname', 'PIFirstName', 'Title', 'Email', 'CondensedTitle']]

        # Save the processed data into a new spreadsheet
        output_file = 'processed_research_projects.xlsx'  # Update this to your output file
        output_df.to_excel(output_file, index=False)

        print("Processing complete. Output saved to", output_file)



