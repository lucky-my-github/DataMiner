from pydriller import Repository

class Project:

    def __init__(self, name, url, branch, starting_commit, ending_commit):
        self.name = name
        self.url = url
        self.branch = branch
        self.starting_commit = starting_commit
        self.ending_commit = ending_commit

        #{auto_name: the number of modified files}
        self.author_modified_files = {}
        self.commit_most_modified_lines = {'hash': None, 'lines': 0}

    def collect_statistics(self):

        repo = Repository(self.url, from_commit=self.starting_commit)

        # generate only load 1 commit per time
        generator = repo.traverse_commits()  # traverse_commits() method form pydriller

        for commit in generator:
            self.process_commit(commit)

    def process_commit(self, commit):
        author_name = commit.author.name
        modified_files = commit.files

        if author_name in self.author_modified_files:
            #sum whatever modified in that commit
            self.author_modified_files[author_name] += modified_files
        else:
            self.author_modified_files[author_name] = modified_files

        modified_lines = commit.lines
        if self.commit_most_modified_lines['lines'] < modified_lines:
            self.commit_most_modified_lines = {'hash': commit.hash, 'lines': modified_lines}

    def get_statistics(self):
        _hash, _lines = self.commit_most_modified_lines.values()

        author_name = max(self.author_modified_files, key=self.author_modified_files.get)

        return f'Project name: {self.name}:\n ' \
               f'\tThe author with most modification is {author_name} with ' \
               f'{self.author_modified_files[author_name]} modified files.\n' \
               f'\tThe commit with most modified lines is {_hash} with {_lines} modified lines.'