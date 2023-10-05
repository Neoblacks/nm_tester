
import subprocess
import time
import os
import simple_term_menu

def	libft_partA(functions_to_check, function_check_B, part):
	print("\033[1m\033[4mPartie 1\033[0m\n")
	print("\033[93mChecking norme please wait\033[0m\n")
	time.sleep(0.5)
	result = subprocess.run(["norminette"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	norme_check = result.stdout
	#if line start with "Error" print the line and the next one
	lines = norme_check.split("\n")
	no_errors = True
	for i in range(len(lines)):
		if "Error" in lines[i]:
			print(lines[i])
			no_errors = False
			time.sleep(0.04)
	if no_errors != False:
		print("Norme \033[32m\033[4mOK\033[0m")
	print("\n\033[93mChecking forbidden functions please wait\033[0m\n")
	time.sleep(0.5)
	output = subprocess.check_output(["nm", "libft.a"]).decode("utf-8")
	lines = output.split("\n")

	functions_in_library = {}
	functions_in_library_a = {}
	current_file = None

	for line in lines:
		line = line.strip()
		if line.endswith(".o:"):
			current_file = line[:-3]
			functions_in_library[current_file] = []
			if current_file in function_check_B:
				functions_in_library_a[current_file] = []

		elif line.startswith("U") or line.startswith("0"):
			if current_file and current_file in functions_to_check:
				functions_in_library[current_file].append(line)
			elif current_file and current_file in function_check_B:
				functions_in_library_a[current_file].append(line)

	unauthorized_functions = {}

	if part == 1:
		for i in functions_in_library:
			unauthorized_functions[i] = []
			for j in functions_in_library[i]:
				if j.startswith("U") and "ft_" not in j:
					unauthorized_functions[i].append(j)
			if len(unauthorized_functions[i]) > 0:
				for j in unauthorized_functions[i]:
					print(f"\n\033[93m{i} utilise la fonction externe {j}\033[0m\n")
			else:
				print(f"Fichier {i}.c \033[32m\033[4mOK\033[0m")
			time.sleep(0.04)

		unauthorized_functions_a = {}

		for i in functions_in_library_a:
			unauthorized_functions_a[i] = []
			for j in functions_in_library_a[i]:
				if j.startswith("U") and "ft_" not in j and "malloc" not in j:
					unauthorized_functions_a[i].append(j)
			if len(unauthorized_functions_a[i]) > 0:
				for j in unauthorized_functions_a[i]:
					print(f"\n\033[93m{i} utilise la fonction externe {j}\033[0m\n")
			else:
				print(f"Fichier {i}.c \033[32m\033[4mOK\033[0m")
			time.sleep(0.04)
	return

def	libft_partB():
	print("\n\033[1m\033[4mPartie 2\033[0m\n")
	#Print Work in progress
	print("\033[93mWork in progress\033[0m\n")
	return

def	libft():
	option = ["Partie 1/2", "Bonus", "Exit"]
	terminal = simple_term_menu.TerminalMenu(option)
	choice = terminal.show()
	if choice == 0:
		os.system("clear")
		part = 1
		functions_to_check = [
		"ft_isalpha", "ft_isdigit", "ft_isalnum", "ft_isascii", "ft_isprint", "ft_strlen",
		"ft_memset", "ft_bzero", "ft_memcpy", "ft_memmove", "ft_strlcpy", "ft_strlcat",
		"ft_toupper", "ft_tolower", "ft_strchr", "ft_strrchr", "ft_strncmp", "ft_memchr",
		"ft_memcmp", "ft_strnstr", "ft_atoi"
		]
		function_check_B = ["ft_calloc", "ft_strdup"]
		libft_partA(functions_to_check, function_check_B, 1)
	elif choice == 1:
		libft_partB()
	elif choice == 2:
		os.system("clear")

def	printf():
	skip_libft = [
		"ft_atoi","ft_bzero","ft_calloc","ft_isalnum","ft_isalpha","ft_isascii","ft_isdigit","ft_isprint","ft_itoa",
		"ft_lstadd_back","ft_lstadd_front","ft_lstclear","ft_lstdelone","ft_lstiter","ft_lstlast","ft_lstmap",
		"ft_lstnew","ft_lstsize","ft_memchr","ft_memcmp","ft_memcpy","ft_memmove","ft_memset","ft_putchar_fd",
		"ft_putendl_fd","ft_putnbr_fd","ft_putstr_fd","ft_split","ft_strchr","ft_strdup","ft_striteri","ft_strjoin",
		"ft_strlcat","ft_strlcpy","ft_strlen","ft_strmapi","ft_strncmp","ft_strnstr","ft_strrchr","ft_strtrim","ft_substr",
		"ft_tolower","ft_toupper","ft_uitoa",
	]
	result = subprocess.check_output(["nm", "libftprintf.a"]).decode("utf-8")
	lines = result.split("\n")
	functions_in_library = {}
	current_file = None
	for line in lines:
		line = line.strip()
		if line.endswith(".o:"):
			current_file = line[:-3]
			if current_file not in skip_libft:
				functions_in_library[current_file] = []
		elif line.startswith("U") or line.startswith("0"):
			if current_file and current_file not in skip_libft:
				functions_in_library[current_file].append(line)
	unauthorized_functions = {}
	for i in functions_in_library:
		unauthorized_functions[i] = []
		for j in functions_in_library[i]:
			if j.startswith("U") and "ft_" not in j and "malloc" not in j and "free" not in j and "write" not in j and "va_" not in j:
				unauthorized_functions[i].append(j)
		if len(unauthorized_functions[i]) > 0:
			for j in unauthorized_functions[i]:
				print(f"\n\033[93m{i} utilise la fonction externe {j}\033[0m\n")
		else:
			print(f"Fichier {i}.o \033[32m\033[4mOK\033[0m")
		time.sleep(0.04)

def	main():
	option = ["Libft", "Gnl", "Printf", "Exit"]
	terminal = simple_term_menu.TerminalMenu(option)
	choice = terminal.show()
	if choice == 0:
		libft()
	elif choice == 1:
		print("gnl")
	elif choice == 2:
		printf()
	elif choice == 3:
		os.system("clear")
	return

if __name__ == "__main__":
	main()
