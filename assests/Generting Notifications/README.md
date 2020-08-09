## Desktop Notifier Application :heart:

# A desktop notifier application produces a notification system which produces a notification message in the form of a pop up message on the desktop.

Desktop notification is shown even if you are browsing a different tab or you have opened another app, e.g. Microsoft Word. 

**Module used : plyer** , which is used to access the features of the hardware . This module is not built-in , so we have to install it externally in the terminal using *pip install plyer.*

**Syntax** notify(title="string", message="string", app_name="string", app_icon="string", timeout=int, ticker="", toast=bool)

*Now, let us talk about the Parameters :*
*- title ("string") : Title of the notification*
*- message("string") : For the notification message*
*- app_name("string") : Naming that application which is launching this notification*
*- app_icon("string") : For the icon that needs to be displayed along with the message in the pop up notification.*
*- timeout(int) : the time to display the message, by default it is 10*
*- ticker(str) : for displaying the text on the status bar as soon as the arrival of the notification*
*- toast(bool) : This will be a simple android message instead of full notification*


