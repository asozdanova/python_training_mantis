from selenium import webdriver
from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.viewStatus)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)


    project_cache = None

    def delete_project(self,project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//a[text()='%s']" %project.name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None


    def get_projects_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            #self.project_cache = []
            project_list = []
            rows = wd.find_elements_by_xpath("//table[@class='width100']//tr[starts-with(@class, 'row-')]")
            for element in rows[1:]:
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                viewStatus = cells[3].text
                description = cells[4].text
                #self.project_cache.append(Project(name=name, status=status, viewStatus=viewStatus,
                                                  #description=description))
                project_list.append(Project(name=name, id=id,status=status, viewStatus=viewStatus,description=description))
        #return self.project_cache
        return list(project_list)

