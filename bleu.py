
import subprocess
import time
import os
import simple_term_menu
import re

# NORME
			# print("\033[93mChecking norme please wait\033[0m\n")
			# time.sleep(0.5)
			# result = subprocess.run(["norminette"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
			# norme_check = result.stdout
			# lines = norme_check.split("\n")
			# no_errors = True
			# for i in range(len(lines)):
			# 	if "Error" in lines[i]:
			# 		print(lines[i])
			# 		no_errors = False
			# 		time.sleep(0.04)
			# if no_errors != False:
			# 	print("Norme \033[32m\033[4mOK\033[0m")
			# print("\n\033[93mChecking forbidden functions please wait\033[0m\n")
			# time.sleep(0.5)

def	libft_partA(functions_to_check, function_check_B, part):
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
		print("\033[1m\033[4mPartie A\033[0m\n")
		for i in functions_in_library:
			unauthorized_functions[i] = []
			if functions_in_library[i] == []:
				continue
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
			if functions_in_library_a[i] == []:
				continue
			for j in functions_in_library_a[i]:
				if j.startswith("U") and "ft_" not in j and "malloc" not in j:
					unauthorized_functions_a[i].append(j)
			if len(unauthorized_functions_a[i]) > 0:
				for j in unauthorized_functions_a[i]:
					print(f"\n\033[93m{i} utilise la fonction externe {j}\033[0m\n")
			else:
				print(f"Fichier {i}.c \033[32m\033[4mOK\033[0m")
			time.sleep(0.04)
	elif part == 2:
		print("\n\033[1m\033[4mPartie B\033[0m\n")
		time.sleep(0.5)
		malloc_authorized = ["ft_substr", "ft_strjoin", "ft_strtrim", "ft_itoa", "ft_strmapi"]
		free_and_malloc_authorized = ["ft_split"]
		write_authorized = ["ft_putchar_fd", "ft_putstr_fd", "ft_putendl_fd", "ft_putnbr_fd"]
		for i in functions_in_library:
			unauthorized_functions[i] = []
			if functions_in_library[i] == []:
				continue
			for j in functions_in_library[i]:
				if i in malloc_authorized:
					if j.startswith("U") and "ft_" not in j and "malloc" not in j:
						unauthorized_functions[i].append(j)
				elif i in free_and_malloc_authorized:
					if j.startswith("U") and "ft_" not in j and "free" not in j and "malloc" not in j:
						unauthorized_functions[i].append(j)
				elif i in write_authorized:
					if j.startswith("U") and "ft_" not in j and "write" not in j:
						unauthorized_functions[i].append(j)
			if len(unauthorized_functions[i]) > 0:
				for j in unauthorized_functions[i]:
					print(f"\n\033[93m{i} utilise la fonction externe {j}\033[0m\n")
			else:
				print(f"Fichier {i}.c \033[32m\033[4mOK\033[0m")
			time.sleep(0.04)
	return

def	libft_partB(functions_to_check):
	print("\n\033[1m\033[4mPartie 2\033[0m\n")
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
		functions_to_check = [
		"ft_substr", "ft_strjoin", "ft_strtrim", "ft_itoa", "ft_strmapi", "ft_split",
		"ft_putchar_fd", "ft_putstr_fd", "ft_putendl_fd", "ft_putnbr_fd",
		]
		function_check_B = []
		libft_partA(functions_to_check, function_check_B, 2)
	elif choice == 1:
		print("bonus")
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


def	philosophers():
	function_h = os.popen("cat philo.h | grep \"(\" | cut -f 2-4 | sed 's/([^)]*)//;s/;$//'").read()
	function_h = function_h.split("\n")
	for i in range(len(function_h)):
		function_h[i] = function_h[i].strip()
	function_h = list(filter(None, function_h))
	for i in range(len(function_h)):
		if function_h[i] == "":
			del function_h[i]
		else:
			function_h[i] = function_h[i].split("*")[0]
			function_h[i] = function_h[i].split("(")[0]
	function_h = list(filter(None, function_h))

	output = subprocess.check_output(["nm", "philo"]).decode("utf-8")
	lines = output.split("\n")

	authorized_functions = [
		"memset", "printf", "malloc", "free", "write",
		"usleep", "gettimeofday", "pthread_create",
		"pthread_detach", "pthread_join", "pthread_mutex_init",
		"pthread_mutex_destroy", "pthread_mutex_lock",
		"pthread_mutex_unlock"
	]

	function_names = []
	for line in lines:
		line = line.strip()
		if line.startswith("U"):
			function_names.append(line[2:])
	#remove all characters after the @
	for i in range(len(function_names)):
		function_names[i] = function_names[i].split("@")[0]
	#remove function starting with __
	for i in function_names:
		if i.startswith("__"):
			function_names.remove(i)

	# time.sleep(10)

	unauthorized_functions = []

	for i in function_names:
		if i not in authorized_functions and i not in function_h:
			unauthorized_functions.append(i)

	unauthorized_functions = list(filter(None, unauthorized_functions))
	if len(unauthorized_functions) > 0:
		for i in unauthorized_functions:
			print(f"\n\033[93m{i} n'est pas autorisé\033[0m\n")
	else:
		print("\033[32m\033[4mOK\033[0m")

def	main():
	option = ["Libft", "Philosophers", "Printf", "Exit"]
	terminal = simple_term_menu.TerminalMenu(option)
	choice = terminal.show()
	if choice == 0:
		libft()
	elif choice == 1:
		# print("philosophers")
		philosophers()
	elif choice == 2:
		printf()
	elif choice == 3:
		os.system("clear")
	return

if __name__ == "__main__":
	main()
