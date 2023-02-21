from model.project import Project


def test_add_project(app):
    old_projects = app.project.get_projects_list()
    project=Project(name="Test5", status="release", viewStatus="public",
                 description="test",inherit_global=True)
    app.project.create(project)
    new_projects = app.project.get_projects_list()  # новый список проектов
    assert len(old_projects) + 1 == len(new_projects)  # сравнение старых и новых проектов
    old_projects.append(project)
    assert sorted(old_projects, key=(lambda x: x.name)) == sorted(new_projects, key=(lambda x: x.name))

