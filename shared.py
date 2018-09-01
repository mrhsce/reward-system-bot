import os.path


WORK_TYPE = "work"
STUDY_TYPE = "study"
FUN_TYPE = "fun"

WORK_FACTOR = 4
STUDY_FACTOR = 3
FUN_FACTOR = 1

# *****************************************************************************


def update_hours(type, amount):
  global work_total_hour, study_total_hour, fun_total_hour
  if type == WORK_TYPE:
    work_total_hour = round(work_total_hour + amount, 2)
    fun_total_hour = round(fun_total_hour + amount / WORK_FACTOR, 2)
  if type == STUDY_TYPE:
    study_total_hour = round(study_total_hour + amount, 2)
    fun_total_hour = round(fun_total_hour + amount / STUDY_FACTOR, 2)
  if type == FUN_TYPE:
    fun_total_hour = round(fun_total_hour - amount / FUN_FACTOR, 2)

  store_into_file(work_total_hour, study_total_hour, fun_total_hour)


# *********************** File related functions ******************************

def retrieve_from_file():
  try:
    if os.path.exists('rs_vars'):
      f = open("rs_vars", "r")
      contents = f.read().split("\n")
      if len(contents) == 3:
        work_total_hour = float(contents[0].split("= ")[1])
        study_total_hour = float(contents[1].split("= ")[1])
        fun_total_hour = float(contents[2].split("= ")[1])
      f.close()
      return work_total_hour, study_total_hour, fun_total_hour
    else:
        return 0,0,0
  except:
    print("Error reading the file")
    return 0,0,0


def store_into_file(work_total_hour, study_total_hour, fun_total_hour):
  f = open("rs_vars", "w")
  f.write("Work hours" + " = " + str(work_total_hour) + "\n")
  f.write("Study hours" + " = " + str(study_total_hour) + "\n")
  f.write("fun hours" + " = " + str(fun_total_hour))
  f.close()


def get_fun_hours():
    return fun_total_hour

# *****************************************************************************


work_total_hour, study_total_hour, fun_total_hour = retrieve_from_file()
