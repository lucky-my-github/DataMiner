from repository_loader import RepositoryLoader
from settings import Settings
from git_miner import Project

class Main:

    def __init__(self):
        self.repository = []
        self.settings = Settings()

    def _load_project(self):  #with _ begin means we can only use this method in this class
        projects = []

        repository_loader = RepositoryLoader(self.settings.get_repository_file_path())
        loaded_projects = repository_loader.load()

        for p in loaded_projects:
            project = Project(
                p["repo_name"],
                p["git_url"],
                p["branch"],
                p["starting_commit"],
                p["ending_commit"]
            )
            projects.append(project)
        return projects

    def start(self):
        # loading the _load_project
        # collect the stats
        # print the author and the commit hash
        projects = self._load_project()
        for project in projects:
            project.collect_statistics()
            print(str(project.get_statistics()))

main = Main()
main.start()
