import csv


class RepositoryLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        # Inner function to check for empty cells/space
        def get_value(string):
            string = string.strip()  #remove the whitespace from the beginning and end
            if string:
                return string
            else:
                return None

        with open(self.file_path) as repo_file:
            #read everyline in the file as dictionary
            reader = csv.DictReader(repo_file, delimiter = ';', quotechar = '"')
            projects = []
            #saving whatever have in the attribute
            for row in reader:
                project = {
                    "repo_name": get_value(row["repo_name"]),
                    "git_url": get_value(row["git_url"]),
                    "branch": get_value(row["branch"]),
                    "starting_commit": get_value(row["starting_commit"]),
                    "ending_commit": get_value(row["ending_commit"])
                }

                projects.append(project)

            return projects



