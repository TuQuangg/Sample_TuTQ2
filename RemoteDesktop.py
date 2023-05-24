from pywinauto.application import Application
remote_ctr = Application(backend='uia').start(r'C:/WINDOWS/system32/mstsc.exe')
Dialog = remote_ctr.connect(title = 'Remote Desktop Connection', timeout = 100)
showOpt = remote_ctr.Dialog.child_window(title="Show Options ", control_type="Button").wrapper_object()
showOpt.click_input()
Dialog = remote_ctr.connect(title = 'Remote Desktop Connection', timeout = 100)
remote_ctr.Dialog.print_control_identifiers()

pcIP=remote_ctr.Dialog.child_window(title="Computer:", auto_id="13050", control_type="Edit")
pcIP.type_keys('10.46.30.182')

userName = remote_ctr.Dialog.child_window(title="User name:", auto_id="13064", control_type="Edit")
userName.type_keys('FSOFT.FPT.VN\TuTQ2')

connectBtn = remote_ctr.Dialog.child_window(title="Connect", auto_id="1", control_type="Button")
connectBtn.click_input()
print(connectBtn.is_checked())