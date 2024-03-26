import pytest

from Influncers_pages.Git import GitRepo


class Test_Git:
    @pytest.mark.run(order=42)
    def test_git_push(self):
        self.git = GitRepo()
        self.git.push_to_git_repository()
