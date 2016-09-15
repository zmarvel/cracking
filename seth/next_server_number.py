def next_server_number(servers):
	sort_serv = sorted(servers)
	print sort_serv
	for i in range(len(servers) - 1):
		if i + 1 != sort_serv[i]:
			return i + 1
