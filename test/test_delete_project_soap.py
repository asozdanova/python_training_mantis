from model.project import Project
import random


def test_add_project(app):
     app.session.login("administrator", "root")
     if len(app.soap.get_project_list()) == 0:
      app.project.create(Project(name="Test2", status="release", viewStatus="public",
                 description="test",inherit_global=True))
     old_project_list = app.soap.get_project_list()
     project = random.choice(old_project_list)
     app.project.delete_project(project)
     new_project_list = app.soap.get_project_list()
     #assert len(old_project_list) -1 == len(new_project_list)
     assert len(old_project_list) -1 == len(new_project_list)