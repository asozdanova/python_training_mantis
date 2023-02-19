from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_projects_list()
    app.project.create(Project(name="Test2", status="release", viewStatus="public",
                 description="test",inherit_global=True))
    new_projects = app.project.get_projects_list()  # новый список проектов
    assert len(old_projects) + 1 == len(new_projects)  # сравнение старых и новых проектов
