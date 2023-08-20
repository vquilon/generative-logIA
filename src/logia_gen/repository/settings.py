from logia_gen.application.project import LogiaGenProject
from logia_gen.application.definitions import ConfigFiles
from logia_gen.infrastructure.settings import Settings
from logia_gen.repository.definitions import RepoType


class RepoSettings(Settings):
    def __init__(self, logia_gen_project: LogiaGenProject, repo_type: RepoType) -> None:
        super().__init__(
            logia_gen_project.get_config_path(),
            ConfigFiles.REPOSITORY
        )
        self.repo_type = repo_type

        # Initialize common settings
        self.load_settings()

    def load_settings(self):
        # Load common repo settings
        ...