'''
The Category class collects the questions for each topic. It is also the superclass for topics which are the subclasses
'''

from question import Question

class Category
  def __init__(self, topic_name, question)
    self.topic_name = topic_name           #This will be the chosen topic for the game.
    self.question = question               #This will be for the questions.

  def get_topic_name(self):
      '''
      Returns the name of the topic
      '''
      return self.topic_name = self.topic_name
  
  def get_question(self):
      '''
      Returns the questions for that topic
      '''
      return self.question

class Faculty(Category):      #This will inherit the attribute "question" from the Category class
  def __init__(self, name, role):
  super().__init__(question)
  self.name = name
  self.role = role

  def get_name(self):
    '''
    Returns the name of the faculty
    '''
    return self.name

  def get_role(self):
    '''
    Returns the role of the faculty
    '''
    return self.role

class Facilities(Category):     #This will inherit the attribute "question" from the Category class
  def __init__(self, facility_no, facility_name, facility_use):
  super().__init__(question)
  self.facility_no = facility_no
  self.facility_name = facility_name
  self.facility_use = facility_use

  def get_facility_no(self):
    '''
    Returns the facility_no
    '''
    return self.facility_no

  def get_facility_name(self):
    '''
    Returns the facility_name
    '''
    return self.facility_name

  def get_facility_use(self):
    '''
    Returns the facility_use
    '''
    return self.facility_use

class History(Category):     #This will inherit the attribute "question" from the Category class
  def __init_(self, year, rank, first_program, physical_campus, symbol, global_organization):
  super().__init__(question)
  self.year = year
  self.rank = rank
  self.first_program = first_program
  self.physical_campus = physical_campus
  self.symbol = symbol
  self.global_organization = global_organization

  def get_year(self):
    '''
    Returns the year
    '''
    return self.year

  def get_rank(self):
    '''
    Returns the rank
    '''
    return self.rank

  def get_first_program(self):
    '''
    Returns the first program
    '''
    return self.first_program

  def get_physical_campus(self):
    '''
    Returns the phyical campus
    '''
    return self.physical_campus

  def get_symbol(self):
    '''
    Returns the symbol
    '''
    return self.symbol

  def get_global_organization(self):
    '''
    Returns the global_organization
    '''
    return self.global_organization

class OnlineLearningSystem(Category):     #This will inherit the attribute "question" from the Category class
  def __init__(self, platform, library, student_org, journal, live_platform, system)
  super().__init__(question)
  self.platform = platform
  self.library = library
  self.student_org = student_org
  self.journal = journal
  self.live_platform = live_platform
  self.system = system

  def get_platform(self):
    '''
    Returns the platform
    '''
    return self.platform

  def get_library(self):
    '''
    Returns the library
    '''
    return self.library

  def get_student_org(self):
    '''
    Returns the student_org
    '''
    return self.student_org

  def get_journal(self):
    '''
    Returns the journal
    '''
    return self.journal

  def get_live_platform(self):
    '''
    Returns the live_platform
    '''
    return self.live_platform

  def get_system(self):
    '''
    Returns the system
    '''
    return self.system
