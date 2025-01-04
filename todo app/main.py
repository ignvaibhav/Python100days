from todo import ToDoList

vaibhav = ToDoList()
vaibhav.adding("Study", "Complete python module")
vaibhav.adding("Edit", "Edit Ben's long video")
vaibhav.adding("Agency", "Coordinate with Editors")

vaibhav.displaying()

vaibhav.update("Agency", True)
vaibhav.displaying()

vaibhav.removing("Agency")
vaibhav.displaying()