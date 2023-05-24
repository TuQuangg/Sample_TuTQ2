import time

from pywinauto.application import Application

zoom_ctrl = Application(backend='uia').start('C:/Users/tutq5/AppData/Roaming/Zoom/bin/Zoom.exe').connect(title = 'Zoom', timeout = 100)
zoom_ctrl.Zoom.print_control_identifiers()
homeTab = zoom_ctrl.Zoom.child_window(title="Home", control_type="TabItem").wrapper_object()
homeTab.click_input()
joinBtn_p = zoom_ctrl.Zoom.child_window(title="Join", control_type="Button").wrapper_object()
joinBtn_p.click_input()


joinWin = Application(backend='uia').connect(title = 'Join Meeting', timeout = 100)
# joinWin.JoinMeeting.print_control_identifiers()
idBox = joinWin.JoinMeeting.child_window(title="Meeting ID or Personal Link Name", control_type="Edit").wrapper_object()
idBox.type_keys('420 596 6412', with_spaces = True)



nameBox = joinWin.JoinMeeting.child_window(title="Enter your name", control_type="Edit").wrapper_object()
nameBox.click_input()
nameBox.type_keys('^a{BACKSPACE}')
nameBox.type_keys('James Smith', with_spaces = True)

joinBtn_c = joinWin.JoinMeeting.child_window(title="Join", control_type="Button").wrapper_object()
joinBtn_c.click_input()

pwWin = Application(backend='uia').connect(title = 'Enter meeting passcode', timeout = 100)
# pwWin.EnterMeetingPasscode.print_control_identifiers()
pw_input = pwWin.EnterMeetingPasscode.child_window(title="Meeting Passcode", control_type="Edit").wrapper_object()
pw_input.type_keys('James Smith', with_spaces = True)

pwWin.EnterMeetingPasscode.child_window(title="Join Meeting", control_type="Button").click_input()
time.sleep(10)
pwWin.EnterMeetingPasscode.child_window(title="Cancel", control_type="Button").click_input()

zoom_ctrl.Zoom.child_window(title="Close", control_type="Button").click_input()

