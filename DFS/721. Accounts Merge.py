721. Accounts Merge

# virtual graph node

class Solution:
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		account_graph = defaultdict(list)

		for acc in accounts:
			# Use first email as the core
			first_email = acc[1]
			if first_email not in account_graph:
				account_graph[first_email]

			for email in acc[2:]:
				account_graph[first_email].append(email)
				account_graph[email].append(first_email)

		# DFS
		def dfs(merged_account, email):
			if email in visited:
				return

			visited.add(email)
			merged_account.append(email)

			for nghbr in account_graph[email]:
				dfs(merged_account, nghbr)


		visited = set()
		res = []

		for acc in accounts:
			name = acc[0]
			first_email = acc[1]
			if first_email not in visited:
				merged_account = [name]
				dfs(merged_account, first_email)
				merged_account[1:] = sorted(merged_account[1:])
				res.append(merged_account)

		return res


		