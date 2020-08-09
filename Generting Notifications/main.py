from plyer import notification


def notifyme(title, message):
	notification.notify(
		title = title,
		message = message,
		timeout = 10
	)



if __name__ == "__main__":
	notifyme(" YOU ARE THE BEST , KEEP IT UP")