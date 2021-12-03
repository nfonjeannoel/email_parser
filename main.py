
def parse_email(text):
    valid_emails = []
    split_text = text.split()
    email_list = [i for i in split_text if "@" in i and i.count('@') == 1]
    for email in email_list:
        beginning = email.split("@")[0]
        end = email.split("@")[-1]
        if len(beginning) > 0 and "." in end and len(end) > 1:
            valid_emails.append(email)
    return valid_emails


if __name__ == '__main__':
    print(parse_email("Schools of Chemistry and Biological Sciences, University of Exeter, Stocker Road, Exeter EX4 4QD, UK. abc@gmail.com@.net  J.A.Little@exeter.ac.uk"))